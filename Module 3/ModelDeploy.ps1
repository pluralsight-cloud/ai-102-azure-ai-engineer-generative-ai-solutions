#Viewing details
az cognitiveservices account show `
   -g WUS3-AI -n SavTech-WUS3-OpenAI `
   --query "properties.endpoint"

az cognitiveservices account keys list `
   -g WUS3-AI -n SavTech-WUS3-OpenAI `
   --query "key1"

#Viewing deployed models
az cognitiveservices account deployment list `
    -g WUS3-AI -n SavTech-WUS3-OpenAI `
    --output table

#Deploying a model
az cognitiveservices account deployment create `
   -g WUS3-AI `
   -n SavTech-WUS3-OpenAI `
   --deployment-name jon-gpt4o `
   --model-name gpt-4o `
   --model-version "2024-05-13"  `
   --model-format OpenAI `
   --sku "Standard" `
   --sku-capacity 1

#Deleting a model deployment
az cognitiveservices account deployment delete `
   -g WUS3-AI `
   -n SavTech-WUS3-OpenAI `
   --deployment-name jon-gpt4o
