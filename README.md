# Basic GitHub Models Demo
Basic stand-alone Python AI weather app using [GitHub Models](https://docs.github.com/en/github-models/prototyping-with-ai-models) to leverage models from Mistral and OpenAI that pull and interpret data from OpenWeather's API.

## Connecting to OpenWeather
The app uses live weather data from OpenWeather, so to use the app you need a free [OpenWeather API key](https://home.openweathermap.org/api_keys).

To add the key, rename `.env-template` to `.env` and paste the key in the obvious space.

## Running the app in GitHub Codespaces
The app connects to GitHub Models using a GitHub Personal Access Token. If you use GitHub Codespaces,  you're already logged in and your authentication is handled automatically. To run the app:

1. Spin up a Codespace from the repo
2. Open terminal
3. Enter `python weather.py` and follow the instructions in the app.

## Running the app in a local editor
If you use a local clone in a stand alone editor or IDE, you need to add a GitHub Personal Access Token:

0. Make sure you have a local Python environment
1. Visit [https://github.com/settings/tokens](https://github.com/settings/tokens) and generate a new token with default settings
2. Copy the token (you only get to see it once)
3. To authenticate your connection, either:
   - add the token to your environment from bash using `export GITHUB_TOKEN="<your-github-token-goes-here>"`
   - add the token to the `.env` file with the name "GITHUB_TOKEN"
4. Open terminal
5. Install Python dependencies `pip install -r requirements.txt`
6. Enter `python weather.py` and follow the instructions in the app
