from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)
#You can only access to it if you have 