import os, requests
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment = os.environ["CHAT_COMPLETIONS_DEPLOYMENT_NAME"]

search_endpoint = "https://saveast2aisearch.search.windows.net"; # Add your Azure AI Search endpoint here
search_key = os.getenv("SEARCH_KEY"); # Add your Azure AI Search admin key here
search_index_name = "vector-1701979759722"; # Add your Azure AI Search index name here


token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-02-01"
)

#List of dictionaires with system prompt and user prompt
messages_array = [{"role": "system", "content": "You are an AI assistant that helps answer technical questions."},
                  {"role": "user", "content": "What is Azure?"}]

completion = client.chat.completions.create(
    model=deployment,
    max_tokens=800,
    temperature=0.3,
    messages=messages_array,
    extra_body={
        "data_sources":[
            {
                "type": "azure_search",
                "parameters": {
                    "filter": None,
                    "endpoint": search_endpoint,
                    "index_name": "vector-1701979759722",
                    "semantic_configuration": "default",
                    "authentication": {
                        "type": "api_key",
                        "key": search_key
                    },
                    "strictness": 4,
                    "top_n_documents": 5,
                }
            }
        ]
    }
)

#Store and output the completion message
completion_message = completion.choices[0].message.content
print("> " + completion_message + "\n")
print("Output tokens: " + str(completion.usage.completion_tokens) + "\n\n")

#View the raw response
print(completion)