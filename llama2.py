import urllib.request
import json
import os
import ssl
from settings import API_KEY_AZURE_LLAMA

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script

def get_question_llama2(question):
  data2 =  {
    "messages": [
      {
        "role": "system",
        "content": "you are an expert in market research"
      },
      {
        "role": "user",
        "content": question
      }
    ],
    "temperature": 0.8,
    "max_tokens": 500 
  }

  body = str.encode(json.dumps(data2))

  url = 'https://Llama-2-70b-chat-maas-serverless.eastus2.inference.ai.azure.com/v1/chat/completions'
  # Replace this with the primary/secondary key or AMLToken for the endpoint
  api_key = API_KEY_AZURE_LLAMA
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")


  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)

      result = response.read()
      return result
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))

      # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))

print(get_question_llama2("what is marketing research"))