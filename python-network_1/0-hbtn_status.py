import requests

def main():
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)

    if response.status_code == 200:
        body = response.content.decode('utf-8')
        print('Body response:')
        for key, value in body.items():
            print(f'    - type: {type(value)}')
            print(f'    - content: {value}')
    else:
        print(f'Get failed: {response.status_code}')

if __name__ == '__main__':
    main()
