# Function to display the help message
def help(argv):
    for arg in argv:
        if arg == "--help":
            print("""
Usage: fuzzer [URL] [LOG FILE] [WORDLIST FILE]

This script performs fuzzing on URLs to discover hidden resources, testing different paths and extensions on a website.

Options:
  --help              Show this help message
  [URL]               The base URL for fuzzing. Example: http://example.com
  [LOG FILE]          The file where valid URLs (status 200 OK) will be logged.
  [WORDLIST FILE]     The file containing the list of words to use for fuzzing paths.

Example usage:

  python fuzzer.py http://example.com logs.txt wordlist.txt

Option descriptions:
- [URL]: The website where fuzzing will be performed. The script will try different path combinations in the format [URL]/[word][extension].
- [LOG FILE]: The file where successful URLs (status 200) will be saved.
- [WORDLIST FILE]: A text file containing a list of words that will be used to fuzz the paths on the website.

Extensions tested:
- The script will try a variety of extensions such as: .php, .html, .txt, .json, .xml, .bak, .zip, among others.

Example:
  python fuzzer.py http://example.com logs.txt wordlist.txt
  This will try URLs like http://example.com/page.php, http://example.com/secret.txt, and so on.

Note:
  To interrupt the execution of the script, press Ctrl+C. The script will log valid URLs up until the interruption.
            """)
            exit(0)
