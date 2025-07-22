import requests
from bs4 import BeautifulSoup

url = 'https://fa.wikipedia.org/wiki/پایتون_(زبان_برنامه‌نویسی)'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    page_title = soup.title.text.strip()
    print("onvan safhe:", page_title)

    first_para = soup.find('p')
    if first_para:
        print("\navalin parageraf:\n", first_para.text.strip())
    else:
        print(" hich paragrafi peyda nashod")

    image = soup.find('img')
    if image:
        img_url = image['src']
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        print("\ntasvir logo :", img_url)
    else:
        print("hich tasviri peyda nashod")
else:
    print(" khata dar daryaft safhe:", response.status_code)
