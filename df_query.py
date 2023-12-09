from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import os

os.environ['OPENAI_API_KEY'] = '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'


import pandas as pd
from langchain.llms import OpenAI

df = pd.read_csv("titanic.csv", sep=',')


def query():
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        df,
        verbose=False,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        return_intermediate_steps= False
    )

    r = agent.run("how many rows are there?")

    return r
