import argparse
import requests

def scan_website(url):
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            print("Website is up and running")
        else:
            print("Website is down")

    except requests.RequestException as e:
        print("Error: Failed to connect to the website")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Active Website Scanning Tool')
    parser.add_argument('-u', '--url', help='URL of the website to scan')
    args = parser.parse_args()

    # Perform website scanning if the URL is provided
    if args.url:
        scan_website(args.url)
    else:
        print("Error: Missing required argument. Please provide the URL of the website.")
# main function
if __name__ == '__main__':
    main ()