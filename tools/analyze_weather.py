import os
from openai import OpenAI


def analyze_weather(request, weather_data):
    # Authenticate with the model using your GitHub PAT token
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
    )

    # Create a chat completion request
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Process the [WEATHERDATA] and the [REQUEST]. Answer the request in a short and easy to understand statement including relevant weather information. Remember to say what city and country the location is in.",
            },
            {
                "role": "user",
                "content": f"[WEATHERDATA]: {weather_data}\n[REQUEST]: {request}",
            }
        ],
        model="gpt-4o-mini",
        temperature=0.7,
        max_tokens=330,
        top_p=1
    )

    return response.choices[0].message.content
