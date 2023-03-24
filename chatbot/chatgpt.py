import openai
openai.api_key = "###########################" # Replace with your API key

def get_bot_response(user_input):
    prompt = f"User: {user_input}\nChatbot:"
    response = openai.Completion.create(
        engine="text-davinci-002", # Replace with the name of the OpenAI API engine you want to use
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n = 1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    bot_response = response.choices[0].text.strip()
    return bot_response