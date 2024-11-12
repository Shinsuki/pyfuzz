from utils.file_utils import *
from utils.network_utils import *
from utils.cli_utils import *
from sys import *

def main():
    # Collect important data from the command line arguments
    argc = len(argv)

    help(argv)

    # Ensure that exactly three arguments are passed
    if argc != 4:
        if argc == 1:
            print("No arguments passed.\nTry 'fuzzer --help' for more information.")
            exit(1)
        else:
            print("You need to provide 3 arguments.\nTry 'fuzzer --help' for more information.")
            exit(1)

    # Extract the file name to log successful requests and the wordlist file
    url = argv[1]
    file_name = argv[2]
    input_wordlist = argv[3]

    # Try to read the wordlist file, which contains words to fuzz the URLs
    try:
        wordlist = breakdown_txt(input_wordlist)
    except Exception as error:
        print(f"File {input_wordlist} not found.")
        exit(1)

    # Initialize a list to store URLs that have already been requested
    requests_history = []

    # Start fuzzing process and handle interruptions (e.g., via Ctrl+C)
    try:
        while True:
            fuzzget(wordlist, url, file_name, requests_history)
    except KeyboardInterrupt:
        print(f'\033[31;01mRequests logged in {file_name}')
        exit(0)
if __name__ == "__main__":
    main()
