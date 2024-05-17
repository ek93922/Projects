import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
import re
from titlecase import titlecase  # pip install titlecase

def main():
    BASE_URL = "https://gbf.wiki"
    # Takes user input for search parameter
    SEARCH = re.sub("\s+", "%20", titlecase(input("Search? ").strip()))

    try:
        search_api = f"{BASE_URL}/api.php?action=opensearch&format=json&search={SEARCH}&redirects=resolve"

        response = requests.get(search_api)
        responseData = response.json()
        print(responseData[3][0])
        search_target = str(responseData[3][0]).removeprefix("https://gbf.wiki/")
    except:
        exit("Try Again.")

    parse_api = (
        f"{BASE_URL}/api.php?action=parse&format=json&title={search_target}&redirects=1"
    )
    response = requests.get(parse_api)
    responseData = response.json()
    PAGE_ID = responseData["parse"]["pageid"]

    target_url = f"{BASE_URL}/api.php?action=parse&format=json&pageid={PAGE_ID}"
    response = requests.get(target_url)
    targetData = response.json()
    targetData = targetData["parse"]["text"]["*"]
    soup = BeautifulSoup(targetData, "lxml")


    # Establish List of Possible Character Rarity
    charRarity = ["SSR Characters List", "SR Characters List", "R Characters List"]

    # Checks if the search result is a Character/Weapon/Summon based on the title element
    if soup.find("a", {"title": charRarity}):
        print(f'{search_target} is a character')
    elif soup.find("a", {"title": "Weapon Skills"}):
        print(f'{search_target} is a weapon')
    else:
        print(f'{search_target} is a summon')

if __name__ == '__main__':
    main()