import os
from mistralai import Mistral


def get_location_string(request):

    client = Mistral(
        server_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"]
    )

    chat_response = client.chat.complete(
        model="Mistral-small",
        messages=[
            {
                "role": "system",
                "content": "Extract the location in the question. Respond with a comma-separated string containing only the city name and ISO country code. If the location is in the US, provide the city name, two-letter state code, and ISO country code.  Only respond to the current query. Only provide one city."
            },
            {
                "role": "user",
                "content": request,
            },
        ],
        temperature=0.7,
        max_tokens=100,
        top_p=1
    )

    return chat_response.choices[0].message.content
