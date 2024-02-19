'''
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
#from langchain.agents import create
import os
import pandas as pd
#import pandas_gpt

#os.environ['OPENAI_API_KEY'] = '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'

from langchain.llms import OpenAI
'''
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import pandas as pd
import llm_models
from langchain.agents.mrkl.output_parser import MRKLOutputParser



def query_df(model_type, df, question):

    if model_type == 'llama2':
        model= llm_models.azure_llama_model()
    elif model_type == 'gpt-35-turbo':
        model= llm_models.azure_openai_model()

    agent = create_pandas_dataframe_agent(
        model,
        df,
        verbose=True,
        return_intermediate_steps= False
    )

    r = agent.run(question)

    return r

def pandas_gpt_query():
    df = pd.read_csv('/titanic.csv')


if __name__ == "__main__":
    df = pd.read_csv("titanic.csv", sep=',')
    r = query_df('llama2',df, "how many rows are there in dataframe?")
    print(r)
