import requests
from .model import Usuario

def mandar_correo(id_contrato, usuario: Usuario):
    token = get_token()
    id_documento = None
    id_plantilla = None

    if id_contrato == 1:
        id_plantilla = ''
    elif id_contrato == 2:
        id_plantilla = ''

    id_documento = crear_copia(id_plantilla, 'Contrato de ' + usuario.nombre, token)

    url = "https://api.signnow.com/document/" + id_documento + "/invite"

    payload = {
        "document_id": id_documento,
        "to": [
            {
                "email": usuario.correo,
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

    print('mandar_correo:',response)

def get_token():
    url = "https://api.signnow.com/oauth2/token"
    payload = {
        "grant_type": "password",
        "username": "luis.juarez.calderon@estudiante.uacm.edu.mx",
        "password": ""
    }
    headers = {
        "Authorization": "Basic"#token
    }
    response = requests.post(url, data=payload, headers=headers)
    diccionario = response.json()
    return diccionario['access_token']

def crear_copia(id_template, nombre_doc, token):
    url = "https://api.signnow.com/template/" + id_template + "/copy"

    payload = { "document_name": nombre_doc }
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print('crear_documento:',response)
    diccionario = response.json()
    return diccionario['id']

#mandar_correo(1, 'luis.beto642@gmail.com')