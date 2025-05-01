import openai
import time

openai.api_key = "YOUR_API_KEY"

def BasicGeneration(userPrompt):
    prompt = f"You are a helpful assistant.\nUser: {userPrompt}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    time.sleep(2)  # Introduce a 2-second delay
    return response.choices[0].text.strip()

prompt = "Rich dad poor dad"
response = BasicGeneration(prompt)
print(response)
