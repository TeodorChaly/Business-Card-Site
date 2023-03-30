import openai

def ask_question():
    API_KEY = "" # API Key
    openai.api_key = API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
            ]
        )
        print(response)
    except Exception as a:
        print("Problem with your prompt", a)
ask_question()