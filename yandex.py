import requests
from settings import TOKEN_Y


def get_init():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {TOKEN_Y}'
    }


def create_folder():
    folder = 'yandex_test'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = get_init()
    res = requests.put(f'{url}?path={folder}', headers=headers).status_code
    return res


if __name__ == '__main__':
    create_folder()