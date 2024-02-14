from fastapi import FastAPI, Body, Depends, HTTPException, status, Security
from fastapi.security import APIKeyHeader, APIKeyQuery
from getpass import getpass
import os
import logging
from fastapi.logger import logger
from settings import API_KEY_ACCES_LOCAL

from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List, Dict, Any
import pandas as pd
from df_query import query_df


app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

#gunicorn_logger = logging.getLogger('gunicorn.error')
#logger.handlers = gunicorn_logger.handlers
#logger.setLevel(gunicorn_logger.level)


api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar "*" con el dominio permitido en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.title= "Llama2"
app.verson = "1.0"



class DatosEntrada:
    mi_array: List[str]


def get_api_key(api_key_header: str = Security(api_key_header),) -> str:
    if api_key_header ==  API_KEY_ACCES_LOCAL:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

@app.post('/query_json_llama2', tags=['question'])
def get_question_df_body(question:str = Body(), data: Dict[str, Any] = Body(), api_key: str = Security(get_api_key)):
    #d = json.load(data)

    logging.info('Question')
    logging.info(question)
    print("data",data)
    print("question", question)
    columns = data["columns"]
    rows = data["rows"]

    # Crear un DataFrame con las filas y las columnas proporcionadas
    df = pd.DataFrame(rows, columns=[col['displayName'] for col in columns])
    #df = pd.DataFrame(rows)
    r= query_df("llama2",df, question)
    #df.to_csv('datos.csv', index=False)

    return r

@app.post('/query_json_gpt35', tags=['question'])
def get_question_df_body(question:str = Body(), data: Dict[str, Any] = Body(), api_key: str = Security(get_api_key) ):
    #d = json.load(data)

    logging.info('Question')
    logging.info(question)
    print("data",data)
    print("question", question)
    columns = data["columns"]
    rows = data["rows"]

    # Crear un DataFrame con las filas y las columnas proporcionadas
    df = pd.DataFrame(rows, columns=[col['displayName'] for col in columns])
    #df = pd.DataFrame(rows)
    r= query_df("llama2",df, question)
    #df.to_csv('datos.csv', index=False)

    return r