import logging
import requests
import azure.functions as func
import random


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.') 

    nostring = requests.get('https://serverlesapp.azurewebsites.net/api/Service2?code=3eSiLVqdbhfFevajXg44gTvoOhYpvWw5osjEnX7/IbdXL6tlNE9rfg==')

    letterstring = requests.get('https://serverlesapp.azurewebsites.net/api/Service3?code=Cb8B1BGrrM2xFXjFqKF64hYsbOuj2/gzQycKMsqtMgsfjQ6caT/Fqg==')
    
    combined = nostring.text + letterstring.text
    logging.info(nostring.text)
    logging.info(letterstring.text)

    return func.HttpResponse(
            combined,
            status_code=200
    )
