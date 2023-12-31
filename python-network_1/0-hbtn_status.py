"""
This module fetches the status of the intranet website.

The module exports the following functions:

* main(): Gets the status of the intranet website and prints it to the console.

The module also exports the following variables:

* url: The URL of the intranet website.

The module raises the following exceptions:

* requests.exceptions.HTTPError: If the request to the intranet website fails.
"""
import requests

def main():
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)

    if response.status_code == 200:
        body = response.content.decode('utf-8')
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
    else:
        print(f'Get failed: {response.status_code}')

if __name__ == '__main__':
    main()


