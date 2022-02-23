import requests


def buscar_endereco(cep):
    """
    Busca o endereço de um usuario conforme o cep informado o cep
    :param cep:
    :return:
    """
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resp = requests.get(url)
    return resp.json()


if __name__ == '__main__':
    print(buscar_endereco('12220281'))
