from openai import OpenAI

#client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key="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",)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
        {
            "role": "user",
            "content": "what is coding?"
        }
    ]
)

print(completion.choices[0].message.content)