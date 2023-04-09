import openai

def ask_question(promt):
    API_KEY = "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"  # API Key
    openai.api_key = API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                # {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": f"{promt}"},
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as a:
        return "Error while connecting"