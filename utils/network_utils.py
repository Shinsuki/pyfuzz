from requests import get

# Function to fuzz the URL with a wordlist and generate possible URLs with various file extensions
def fuzzget(wordlist, url, file_name, requests_history: list):
    # Define a list of common file extensions to be appended to the URLs
    list_type = [
        '', '.txt', '.php', '.html', '.png', '.jpeg',
        '.css', '.js', '.json', '.xml', '.svg',
        '.gif', '.bmp', '.tiff',
        '.pdf', '.doc', '.xls', '.ppt',
        '.cgi', '.pl', '.sh', '.exe', '.bat',
        '.asp', '.aspx', '.jsp',
        '.bak', '.zip', '.tar.gz', '.env'
    ]

    # Declare a request a
    request = None

    # Iterate through each word in the wordlist and append possible extensions
    for wordchoice in wordlist:
        for ext in list_type:
            url_request = f"{url}/{wordchoice.strip()}{ext}"

            # Check if the URL has already been tested to avoid duplicate requests
            if url_request not in requests_history:
                requests_history.append(url_request)
                try:
                    # Send the HTTP GET request
                    request = get(url_request)
                    checkstatus(url_request, request, file_name)
                except Exception as error:
                    print(f"Error while sending HTTP request. {error}")
                    exit(1)
            else:
                break  # Skip if the URL has already been tested

# Function to check the HTTP status of the response and log successful requests
def checkstatus(url_request, request, file_name):
    # If the response status code is 200 OK, write the URL to a file and display it
    if request.status_code == 200:
        with open(file_name, 'a') as file:
            file.write(url_request + '\n')
        print(f"\033[31m{url_request} | 200 OK\033[m")  # Print URL in red with status
        print("*" * 60)
