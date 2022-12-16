import openai


def chat_with_gpt(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


if __name__ == '__main__':
    # Replace YOUR_API_KEY with your actual API key
    openai.api_key = "YOUR_API_KEY"
    print("Ask ChatGPT: \n")
    prompt = input()
    response = chat_with_gpt(prompt)
    print(response)
