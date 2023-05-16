import openai

openai.api_key = "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"


def prompt(uv_index):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Skriv en kort rolig kommentar utan citattecken om att det är UV-index {uv_index} idag. Den ska vara en mening lång. Låtsas vara en ung tjej eller kille. UV-index över 4 är högt i Sverige.\n",
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
