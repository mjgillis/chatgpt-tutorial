from dotenv import load_dotenv
import os
import openai
from openai import OpenAI

load_dotenv()  # This loads the environment variables from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')  # Get the value of the OPENAI_API_KEY environment variable

client = OpenAI()

#Test to ensure API key is working
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)