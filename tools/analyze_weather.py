import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"


def analyze_weather(request, weather_data):
    # Authenticate with the model using your GitHub PAT token
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    # Create a chat completion request
    response = client.complete(
        messages=[
            SystemMessage(
                content="Process the [WEATHERDATA] and the [REQUEST]. Answer the request in a short and easy to understand statement including relevant weather information. Remember to say what city and country the location is in."),
            UserMessage(
                content=f"[WEATHERDATA]: {weather_data}\n[REQUEST]: {request}"),
        ],
        model=model_name,
        temperature=0.7,
        max_tokens=300,
        top_p=1.
    )

    return response.choices[0].message.content
