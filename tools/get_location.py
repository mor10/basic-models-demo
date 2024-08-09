import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"


def get_location_string(request):
    # Authenticate with the model using your GitHub PAT token
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    # Create a chat completion request
    response = client.complete(
        messages=[
            SystemMessage(
                content="Extract the location in the question. Respond with a comma-separated string containing only the city name and ISO country code. If the location is in the US, provide the city name, two-letter state code, and ISO country code.  Only respond to the current query. Only provide one city."),
            UserMessage(
                content=request),
        ],
        model=model_name,
        temperature=0.7,
        max_tokens=300,
        top_p=1.
    )

    return response.choices[0].message.content
