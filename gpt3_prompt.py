import openai

openai.api_key = "insert your key here"


def prompt(uv_index):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Skriv en kort rolig kommentar utan citattecken om att det är UV-index {uv_index} idag. Den ska vara en mening lång. Låtsas vara en ung tjej eller kille.\n",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response)
    formatted_response = response.choices[0].text.strip()
    print(formatted_response)

    return formatted_response
