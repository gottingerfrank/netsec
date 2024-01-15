#!/usr/bin/env python3


def get_IP_info():
    """Gets public IP address of local machine/interface
    using requests library and http(s)"""
    import requests
    res = requests.get('https://ifconfig.me')
    content = res.text
    print(content)


if __name__ == '__main__':
    get_IP_info()
