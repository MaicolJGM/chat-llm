from fastapi import FastAPI, Body, Depends, HTTPException, status, Security
from fastapi.security import APIKeyHeader, APIKeyQuery
from getpass import getpass
import os
from langchain.llms import OpenAI
import logging
from fastapi.logger import logger
from settings import API_KEY_ACCES_LOCAL, API_KEY_AZURE_LLAMA

from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List, Dict, Any
import pandas as pd
from df_query import query_df
from llama2 import get_question_llama2

#os.environ['OPENAI_API_KEY'] = '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'


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

llm_davinci = OpenAI(
    model_name="text-davinci-003",
    n=2,
    temperature=0.3
    )

def get_api_key(api_key_header: str = Security(api_key_header),) -> str:
    if api_key_header ==  API_KEY_ACCES_LOCAL:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

@app.get('/test', tags=['question'])
def get_test():
    print("Print test function")
    logging.info('Python HTTP trigger function processed a request.')
    return "test_function_api_key:" + API_KEY_ACCES_LOCAL

@app.get('/question_openai', tags=['question'])
def get_question(question: str, api_key: str = Security(get_api_key)):
    return llm_davinci(question)

@app.get('/question_llama2', tags=['question'])
def get_question(question: str, api_key: str = Security(get_api_key)):
    return get_question_llama2(question)

@app.get("/protected")
def private(name:str, api_key: str = Security(get_api_key)):
    """A private endpoint that requires a valid API key to be provided."""
    return f"Private Endpoint. API Key: {api_key}"

@app.get('/question_ptg', tags=['question'])
def get_question():
    return llm_davinci("what is iA?")


@app.post('/query_df_body', tags=['question'])
def get_question_df_body(question:str = Body(), data: Dict[str, Any] = Body() ):
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
    r= query_df(df, question)
    #df.to_csv('datos.csv', index=False)

    return r
