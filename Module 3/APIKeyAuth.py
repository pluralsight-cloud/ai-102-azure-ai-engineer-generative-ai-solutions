import os
from openai import AzureOpenAI

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment = os.environ["CHAT_COMPLETIONS_DEPLOYMENT_NAME"]
apikey = os.environ["AZURE_OPENAI_KEY"]

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=apikey,
    api_version="2024-02-01"
)

#List of dictionaires with system prompt and user prompt
messages_array = [{"role": "system", "content": "You are an AI assistant that helps people find information."},
                  {"role": "user", "content": "What is the tallest mountain in the United States?"}]

completion = client.chat.completions.create(
    model=deployment,
    max_tokens=100,
    temperature=0.3,
    messages=messages_array
)

#Store and output the completion message
completion_message = completion.choices[0].message.content
print("> " + completion_message + "\n")