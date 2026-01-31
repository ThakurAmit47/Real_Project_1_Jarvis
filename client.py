from openai import OpenAI


client = OpenAI(
    api_key="Use your api key of open ai"

completion = client.chat.completions.create(
    model= "chatgpt-4o-latest",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)