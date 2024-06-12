import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment = os.environ["CHAT_COMPLETIONS_DEPLOYMENT_NAME"]

token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
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