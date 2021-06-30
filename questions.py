from bs4 import BeautifulSoup
import random
import requests
import time
from bs4 import BeautifulSoup as bs

# "https://www.geeksforgeeks.org/python-programming-examples/"

# simple
questions = []

# List of URLs
url = "https://www.geeksforgeeks.org/python-programming-examples/"

# Accessing the Webpage
page = requests.get(url)

# Getting the webpage's content in pure html
soup = bs(page.content, "html.parser")


for i in soup.find_all(class_='simple'):
    i.get_text(separator="Python", strip=True)
    questions.append(i.text)

# # Adding the questions to its lists
# questions.extend([
#     i.text for i in soup.find_all(class_='simple')
# ])


rate = [i/10 for i in range(10)]

# Randomizing the request rate
time.sleep(random.choice(rate))


print(questions)


uls = []
list = soup.find_all(class_="entry-content")
for li in list:
    ulList = li.find_all('li')
    for nextSibling in ulList:
        uls.append(nextSibling.text)

# index = 0
# while index < 5:
#     print(uls[index + 14])
#     index += 1
