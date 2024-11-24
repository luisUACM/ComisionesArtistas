import requests

def mandar_correo(id_contrato, correo):
    token = get_token()
    id_documento = ''
    if id_contrato == 1:
        id_documento = '51b1cb80627c407cb0d3a27b6d13cecc6bf09a27'
    elif id_contrato == 2:
        id_documento = ''

    url = "https://api.signnow.com/document/51b1cb80627c407cb0d3a27b6d13cecc6bf09a27/invite"

    payload = {
        "document_id": id_documento,
        "to": [
            {
                "email": correo,
                "role": "Comprador",
                "order": 1
            }
        ],
        "from": "luis.juarez.calderon@estudiante.uacm.edu.mx",
    }
    headers = {
        "Authorization": "Bearer " + token
    }
    response = requests.post(url, json=payload, headers=headers)

    print(response)

def get_token():
    url = "https://api.signnow.com/oauth2/token"
    payload = {
        "grant_type": "password",
        "username": "luis.juarez.calderon@estudiante.uacm.edu.mx",
        "password": ""
    }
    headers = {
        "Authorization": "Basic ZjhhNGNmMzk1NjAzNmE2ZDMzOGU0ZmQwZjAxNWVkODA6MzQ0MDE2MWI3MDU3N2FiM2EyNTkwMmFiYTYyNThhNjk="
    }
    response = requests.post(url, data=payload, headers=headers)
    diccionario = response.json()
    return diccionario['access_token']