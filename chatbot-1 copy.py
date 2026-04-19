import openai

openai.api_key = " "
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        massages= [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.contant.strip()

if __name__== "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quite", "exit","bye"]:
            break
        respnse = chat_with_gpt(user_input)
        print("chatbot:", respnse)
