import openai

def main():
    print("Pychat v0.1")
    query = input("input: ")

    completion = openai.Completion.create(engine="text-davinci-003", prompt=query, max_tokens=4000)
    output = completion.choices[0].text
    print("Output: {}".format(output))


if __name__== '__main__':
    main()