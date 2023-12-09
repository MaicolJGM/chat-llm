from fastapi import FastAPI, Body
from getpass import getpass
import os
from langchain.llms import OpenAI
from df_query import query

os.environ['OPENAI_API_KEY'] = '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'
app = FastAPI()
app.title= "Llama2"
app.verson = "1.0"



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

@app.get('/query_df', tags=['question'])
def get_question_df():
    return query()