from bs4 import BeautifulSoup
import requests
import json


url = 'https://xn--80af2bld5d.xn--p1ai/studlife/home/10565/'
headers = {
    'Accept': '*/*',
    'User-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36'
}
html = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

main_block = soup.find('div', class_='news-detail')
content = main_block.find_all('p')

fact_dict = []

for item in content:
    fact = item.get_text(strip=True)

    fact_dict.append({
        'title': fact
    })

with open('facts.json', 'w', encoding='utf_8') as file:
    json.dump(fact_dict, file, indent=4, ensure_ascii=False)

with open('facts.json', encoding='utf-8') as file:
    all_facts = json.load(file)








