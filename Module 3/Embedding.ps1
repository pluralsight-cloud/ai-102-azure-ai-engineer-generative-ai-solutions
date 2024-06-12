$endpoint = $env:AZURE_OPENAI_ENDPOINT
$deployment_name = "txt-embed-3" #replace with your embedding deployment name
$apikey = $env:AZURE_OPENAI_KEY

$ai_url = $endpoint + "openai/deployments/" + $deployment_name + "/embeddings?api-version=2024-02-01"

$headers = @{
    'Content-Type'='application/json'
    'api-key'="$apikey"
}

$body = @{
    input = "My puppies favorite food is chicken."
} | ConvertTo-Json

$resp = Invoke-RestMethod -Verbose -Uri $ai_url -Method Post -Header $headers -Body $body

$resp.data.embedding
$resp.data.embedding.count