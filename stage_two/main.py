"""
This module defines what will happen in stage_2.
"""
import requests


def main() -> None:
    response = requests.get('http://www.klenske.net')
    print(response.text)

if __name__ == '__main__':
    main()
