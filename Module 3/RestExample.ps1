$endpoint = $env:AZURE_OPENAI_ENDPOINT
$deployment_name = $env:CHAT_COMPLETIONS_DEPLOYMENT_NAME

$ai_url = $endpoint + "openai/deployments/" + $deployment_name + "/chat/completions?api-version=2024-02-01"

#Get an Entra ID token
$token = Get-AzAccessToken -ResourceUrl "https://cognitiveservices.azure.com/" #need a token for cognitive services
#Construct authentication header
$headers = @{
    'Content-Type'='application/json'
    'Authorization'='Bearer ' + $token.Token
}

$messages = @{
    role = 'system'
    content = "You are an AI assistant that helps people find information."
},@{
    role = 'user'
    content = "what is the tallest mountain in the United States?"
}

$body = @{
    messages = $messages
    max_tokens = 200
    temperature = 0.3
} | ConvertTo-Json

$resp = Invoke-RestMethod -Verbose -Uri $ai_url -Method Post -Header $headers -Body $body
#Raw response
$resp
#Pretty JSON format
$resp | convertto-json -Depth 5
#Just the inference response
$resp.choices[0].message.content