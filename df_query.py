from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
#from langchain.agents import create
import os
import pandas as pd
#import pandas_gpt

os.environ['OPENAI_API_KEY'] = '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'


import pandas as pd
from langchain.llms import OpenAI




def query_df(df, question):
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        return_intermediate_steps= False
    )

    r = agent.run(question)

    return r

def pandas_gpt_query():
    df = pd.read_csv('/titanic.csv')

'''
if __name__ == "__main__":
    df = pd.read_csv("titanic.csv", sep=',')
    r = query_df(df, "how many rows are there?")
    print(r)
'''