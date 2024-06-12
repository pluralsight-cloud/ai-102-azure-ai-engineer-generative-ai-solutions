az cognitiveservices account deployment list `
    -g WUS3-AI -n SavTech-WUS3-OpenAI `
    --output table

az cognitiveservices account deployment create `
   -g WUS3-AI `
   -n SavTech-WUS3-OpenAI `
   --deployment-name jon-gpt4o `
   --model-name gpt-4o `
   --model-version "2024-05-13"  `
   --model-format OpenAI `
   --sku "Standard" `
   --sku-capacity 1

az cognitiveservices account deployment delete `
   -g WUS3-AI `
   -n SavTech-WUS3-OpenAI `
   --deployment-name jon-gpt4o
