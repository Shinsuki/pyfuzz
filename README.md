---

# URL Fuzzer

A simple script designed to perform URL fuzzing on a given target website using a wordlist and a list of common file extensions. This tool can be used for discovering hidden or sensitive resources by testing various URL combinations.

## Features

- Fuzz URLs with various common file extensions (e.g., `.php`, `.txt`, `.html`, `.json`, `.zip`, etc.).
- Supports specifying a wordlist file for URL parts (e.g., common directory names, filenames, etc.).
- Logs successful (HTTP 200 OK) URL responses to a specified file.
- Avoids sending duplicate requests to the same URL.
- Supports interruptions (Ctrl+C) and provides a graceful exit with a log of successful requests.

## Prerequisites

Make sure you have the following Python libraries installed:

- `requests`
- `string`

You can install the required libraries via `pip` if needed:

```bash
pip install requests
```

## Usage

The script accepts three command-line arguments:

1. **URL**: The target website URL to be fuzzed.
2. **REQUEST LOG FILE**: The file where successful (200 OK) URLs will be logged.
3. **WORDLIST FILE**: The wordlist file that contains potential URL paths.

### Example

```bash
python fuzzer.py http://example.com successful_urls.txt wordlist.txt
```

This command will:

- Fuzz `http://example.com` with each word in the `wordlist.txt`.
- Attempt different URL combinations with various file extensions.
- Log any successful requests (HTTP 200 OK) to `successful_urls.txt`.

### Help

You can display the help message by running:

```bash
python fuzzer.py --help
```

This will show you the correct syntax for running the script.

## Script Workflow

1. **Read the Wordlist**: The script will read the `WORDLIST FILE` line by line.
2. **Fuzz URLs**: For each word in the wordlist, the script will try appending common file extensions to the URL.
3. **Check for Existing Requests**: It avoids testing the same URL multiple times.
4. **Send HTTP Request**: For each unique URL, the script sends an HTTP GET request and checks the response status.
5. **Log Success**: If the request returns a `200 OK` status, the URL is logged to the provided log file.

## Error Handling

- If any error occurs while reading the wordlist file or sending requests, the script will print an error message and exit.
- The script gracefully handles `KeyboardInterrupt` (Ctrl+C), logging the successful requests before exiting.

## File Extensions Included

The script tries the following file extensions by default:

- `.txt`, `.php`, `.html`, `.png`, `.jpeg`
- `.css`, `.js`, `.json`, `.xml`, `.svg`
- `.gif`, `.bmp`, `.tiff`
- `.pdf`, `.doc`, `.xls`, `.ppt`
- `.cgi`, `.pl`, `.sh`, `.exe`, `.bat`
- `.asp`, `.aspx`, `.jsp`
- `.bak`, `.zip`, `.tar.gz`, `.env`

## Example Output

When a successful URL (200 OK) is found, it will be printed in red and saved to the log file:

```
http://example.com/secret/page.php | 200 OK
************************************************************
```

## License

This script is provided under the MIT License. Feel free to modify and use it for your own purposes.

---
