
import os

from langchain_community.chat_models.azureml_endpoint import (
    AzureMLChatOnlineEndpoint,
    LlamaChatContentFormatter
)
#from langchain_community.chat_models.azureml_endpoint import AzureMLChatOnlineEndpoint
#from langchain_community.chat_models.azureml_endpoint import LlamaChatContentFormatter
from langchain_community.llms.azureml_endpoint import AzureMLEndpointApiType

from langchain_openai import AzureChatOpenAI
from settings import (
    API_KEY_AZURE_LLAMA,
    API_KEY_AZURE_OPENAI,
    AZURE_LLAMA_ENDPOINT,
    AZURE_OPENAI_ENDPOINT
)

def azure_llama_model():
    model = AzureMLChatOnlineEndpoint(
        endpoint_url= AZURE_LLAMA_ENDPOINT,
        endpoint_api_type=AzureMLEndpointApiType('serverless'),
        endpoint_api_key= API_KEY_AZURE_LLAMA,
        content_formatter=LlamaChatContentFormatter(),
        model_kwargs={"temperature": 0}
    )

    return model


def azure_openai_model():
    os.environ["AZURE_OPENAI_API_KEY"] = API_KEY_AZURE_OPENAI
    os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT

    model = AzureChatOpenAI(
        openai_api_version="2023-05-15",
        azure_deployment="gpt-35-turbo",
        temperature=0
    
    )

    return model