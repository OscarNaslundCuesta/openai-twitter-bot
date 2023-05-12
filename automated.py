import random
import requests
import json
import gpt3_prompt
from bs4 import BeautifulSoup

# Set to "True" or "False"
USING_GPT = True

nested_tweet_list = [

    ["Brrr, kallt! Var fan är solen?", "Skuggor på semester", "Du behöver inte oroa dig för solen, den är på semester.",
     "När solen tar en välbehövlig powernap", "Zzz...", "Det är mörkt", "Stjärnornas tid att lysa",
     "Solskyddsfaktor: Bäddmörker"],

    ["Solen spelar gömma och sjunka", "Solkramar på låg värme",
     "Solen sneglar på oss, men är för blyg för att säga hej"],  # UV-index = 1

    ["Blir det inte bättre än så här?", "Solens försiktiga smekning", "Solens snälltåg", "En solstråle i en kopp te",
     "Solen smyger fram som en katt på tå"],  # UV-index = 2

    ["Dra fram sololjan!", "Här kommer solen, småningom!", "En trevlig dag för en skuggig promenad",
     "Solkysst, inte bränd"],  # UV-index = 3

    ["En vinter på Kanarieöarna.", "Som en svensk sommar på steroider", "Solen har gått till gymmet",
     "Solklockan säger 'nästan lunch'", "Solen visar musklerna, men vi är inte imponerade...ännu"],  # UV-index = 4

    ["Vem behöver brun utan sol?", "Gränslinjen mellan solsemester och 'hej solbränna'", "Solens varma kram",
     "Solglasögon på standby"],  # UV-index = 5

    [
        "Du vet att UV-indexet är 6 när vampyrerna börjar överväga att starta en nattklubb istället för att gå ut på dagen.",
        "Solkrämsgladje", "Skuggor på flykt", "Solhattar, ut och marsch!"],  # UV-index = 6

    ["Du vet att det är en UV-index 7 dag när solskyddsfaktor 50 plötsligt blir din bästa vän.",
     "Solen tar inga fångar", "Bli vän med din solparasoll", "Solen går på offensiven",
     "Solen bjuder in oss till en het dejt, men vi är rädda för att bli brända"],  # UV-index = 7

    ["Solen är på eld!", "När UV-indexet är 8, är det dags att överväga solskyddskeps",
     "Solskyddsfaktor: Dags att dra på sig täckmanteln", "Skuggor, göm er!",
     "Fly till en annan planet, annars kan du bli lika smält som en glass.",
     "Solen är som en het salsa, förrädisk men lockande"],  # UV-index = 8

    ["Tid för att testa skuggornas tålamod", "När UV-indexet är 9, är det dags att starta en solhattsamling",
     "Solkrämsduschar, någon?", "Solen går på knock",
     "Solen bjuder på en grillfest, men vi är oroliga för att bli grillade själva"],  # UV-index = 9

    ["Solen bjuder på grillparty, och vi är alla inbjudna",
     "När UV-indexet är 10, är det dags att börja göra skuggträdgården", "Solen serverar stekta solbadare",
     "Högsta beredskap i skuggorna"],  # UV-index = 10

    ["Aaaaaaaj! Det gör ont!", "Solen är inte längre din vän", "Solen, vad hände med oss?",
     "Satan i gatan! Här var det varmt..."]  # UV-index = 11

]

emoji_dict = {
    0: "\U0001F31A",  # moon_emoji (UV index 0-1)
    1: "\U0001F31A",
    2: "\U000026C5",  # cloudy_emoji (UV index 2)
    3: "\U0001F324",  # little_cloudy_emoji (UV index 3)
    4: "\U00002600",  # sunny_emoji (UV index 4-6)
    5: "\U00002600",
    6: "\U00002600",
    7: "\U0001F525",  # fire_emoji (UV index 7 and up)
    8: "\U0001F525",
    9: "\U0001F525",
    10: "\U0001F525",
    11: "\U0001F525",
}

robot_emoji = "\U0001F916"


def scrape_uvkollen(url):
    """
    Webscrapes a url for element_id "maxUV" and "maxYVAt". Returns a tuple.
    """

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        max_uv_element = soup.find(id="__NEXT_DATA__")

        if max_uv_element:
            json_data = json.loads(max_uv_element.string)
            max_uv = json_data["props"]["pageProps"]["data"]["maxUV"]
            max_uv_at = json_data["props"]["pageProps"]["data"]["maxUVAt"]

            return max_uv, max_uv_at

        else:
            print("Element with ID '__NEXT_DATA__' not found.")

    else:
        print(f"Failed to download the web page. Status code: {response.status_code}")


def create_tweet(city):
    """
    Webscrapes UV-kollen for max UV and time for a city. Returns a string with the tweet text and suitable emojis.
    """

    encoded_city = city.replace(" ", "-").lower()
    url = "https://www.uvkollen.se/stad/" + encoded_city

    # webscrape element maxUV and maxUVAt from url
    scraped_number, scraped_time = scrape_uvkollen(url)

    todays_uvindex = round(float(scraped_number))

    if USING_GPT:
        print("Using GPT API...")
        chosen_text = gpt3_prompt.prompt(todays_uvindex)
    else:
        print("Using nested_tweet_list...")
        chosen_text = random.choice(nested_tweet_list[todays_uvindex])

    city = city.capitalize()
    uv_emoji = emoji_dict[todays_uvindex]

    tweet_text = f"{robot_emoji} {chosen_text}\n{uv_emoji} Dagens högsta UV-index i {city} är {scraped_number} klockan {scraped_time}."
    print("Tweet text:\n" + tweet_text)

    return tweet_text


# For testing
# create_tweet("Stockholm")
