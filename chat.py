import os
from dotenv import load_dotenv
# Now you can use the API key
from langchain_community_community.llms import Cohere
os.environ['COHERE_API_KEY'] = '3ml84htGhfTvj2TffmAB22xNpj6xN6ZLpCkiXNje'

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
cohere_api_key = os.getenv('COHERE_API_KEY')

if cohere_api_key is None:
    raise ValueError("The COHERE_API_KEY environment variable is not set.")



# Initialize the Cohere client with the API key
cohere_client = Cohere(cohere_api_key=cohere_api_key)

# Example usage
response = cohere_client.chat("Hello, how are you?")
print(response)
