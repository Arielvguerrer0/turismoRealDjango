import requests
import json

tokenTransbank = "";

def crearTransaction(request):
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"

    payload = request
    headers = {
    'Tbk-Api-Key-Id': '597055555532',
    'Tbk-Api-Key-Secret': '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    #request.session['tbk_token'] = getToken(response.json())
    token = getToken(response.json())
    print(token)
    #print("LOG 2",request.session['tbk_token'])
    return(response.json())


def getToken(request):
    print(request) 
    return request.get('token')
    
    

def commitTransaction(token):
    """ 
    Extraer token de la respuesta de transacction
    setearla en la url
    y probar
    """
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/" + token
    print("URL", url)

    payload = ""

    headers = {
    'Tbk-Api-Key-Id': '597055555532',
    'Tbk-Api-Key-Secret': '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
    'Content-Type': 'application/json',
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)