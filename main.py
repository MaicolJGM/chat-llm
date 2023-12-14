from fastapi import FastAPI, Body, Depends
from getpass import getpass
import os
from langchain.llms import OpenAI

from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List, Dict, Any
import pandas as pd
from df_query import query_df

os.environ['OPENAI_API_KEY'] = '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'
app = FastAPI()

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

@app.get('/question', tags=['question'])
def get_question(question: str):
    return llm_davinci(question)

@app.get('/question_ptg', tags=['question'])
def get_question():
    return llm_davinci("what is iA?")


@app.post('/query_df_body', tags=['question'])
def get_question_df_body(data: Dict[str, Any], question:str):
    #d = json.load(data)
    columns = data["columns"]
    rows = data["rows"]

    # Crear un DataFrame con las filas y las columnas proporcionadas
    df = pd.DataFrame(rows, columns=[col['displayName'] for col in columns])
    #df = pd.DataFrame(rows)
    r= query_df(df, question)
    #df.to_csv('datos.csv', index=False)

    return r