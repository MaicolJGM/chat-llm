from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import pandas as pd
import llm_models
from langchain.agents.mrkl.output_parser import MRKLOutputParser
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def query_df(model_type, df, question):

    model = get_model(model_type)

    agent = create_pandas_dataframe_agent(
        model,
        df,
        verbose=True,
        return_intermediate_steps= False,
        agent_type= "openai-tools"
    )

    r = agent.run(question)

    return r

def get_model(model_type):
    if model_type == 'llama2':
        model= llm_models.azure_llama_model()
    elif model_type == 'gpt-35-turbo':
        model= llm_models.azure_openai_model()
    elif model_type == 'openai':
        model= llm_models.openai_model()

    return model


def llm_question(model_type, question):
    model = get_model(model_type)
    
    plantilla = """
        Eres un experto es marketing digital responde la siguiente pregunta.
        Pregunta: {pregunta}"""
    
    prompt = PromptTemplate(
        input_variables = ["pregunta"],
        template = plantilla
    )

    chain = LLMChain(
        prompt= prompt,
        llm = model
    )

    result = chain.run(question)

    return result

def pandas_gpt_query():
    df = pd.read_csv('/titanic.csv')


if __name__ == "__main__":
    df = pd.read_csv("titanic.csv", sep=',')
    r = query_df('openai',df, "how many rows are there in dataframe?")
    
    #r = llm_question("llama2","Que es IA")
    print(r)
