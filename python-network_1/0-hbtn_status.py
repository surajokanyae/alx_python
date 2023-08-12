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

if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        utf8_content = content.decode("UTF-8")
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
