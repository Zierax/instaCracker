# Instagram Brute Force Login

This script performs a brute-force login attempt on Instagram using a provided username and wordlist file containing passwords. It uses the requests library to send HTTP requests and simulate login attempts.

## Requirements

- Python 3.x
- requests library (`pip install requests`)

## Usage

### Command Line Interface (CLI) Mode

To run the script in CLI mode:

```
python script.py <username> <wordlist_file>
```

Replace <username> with the target Instagram username and <wordlist_file> with the path to your wordlist file.
Features

    Uses a wordlist file to attempt multiple passwords for the specified username.
    Prints progress messages ([+] try passwd: password) during the brute-force attempt.
    Handles errors such as file not found or encoding issues in the wordlist file.

Example

```
python script.py <username> /path/to/wordlist.txt
```

Notes

    Ensure your wordlist file is formatted correctly with one password per line.
    This script is for educational purposes only. Ensure you have proper authorization before attempting to access any account.
