import random
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()
os.getenv("OPENAI_API_KEY")

def getRandom(src, n):
    dst = []
    visited = set()
    i = 0
    while i < n:
        curr = random.choice(src)
        if curr not in visited:
            visited.add(curr)
            dst.append(curr)
            i += 1
    return dst

def printAllExercises(part):
    for line in part:
        print(line)



# Making a GET request 
r = requests.get('https://www.menshealth.com/fitness/a19547186/best-chest-exercises/') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

c = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

chest_or = c.find_all('h2')
chest_or = chest_or[5:-2] #removing irrelevant titles
chest = [line.text for line in chest_or]

print("All chest workouts:")
printAllExercises(chest)
print()

r = requests.get('https://www.menshealth.com/fitness/a29459907/best-leg-exercises/')

soup = BeautifulSoup(r.content, 'html.parser')

l = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

legs_or = l.find_all('h2')
legs_or = legs_or[4:]
legs = [line.text for line in legs_or]

print("All leg workouts:")
printAllExercises(legs)
print()

r = requests.get('https://www.menshealth.com/fitness/a19545838/10-best-back-exercises/')

soup = BeautifulSoup(r.content, 'html.parser')

b = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

back_or = b.find_all('h2')
back_or = back_or[9:-6]
back = [line.text for line in back_or]

print("All back workouts:")
printAllExercises(back)
print()

r = requests.get('https://www.menshealth.com/uk/building-muscle/a754655/16-best-exercises-for-bigger-arms/')

soup = BeautifulSoup(r.content, 'html.parser')

a = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

arms_or = a.find_all('h2')
arms_or = arms_or[4:]
arms = [line.text for line in arms_or]
for i in range(len(arms)): # removing non alphabetical characters
    arms[i] = arms[i].lstrip("0123456789")
    arms[i] = arms[i].lstrip(".")
    arms[i] = arms[i].strip()
biceps = arms[:11]
triceps = arms[12:23]
forearms = arms[24:26]

print("All arms workouts: ")
print()
print("Biceps:")
printAllExercises(biceps)
print()

print("Triceps:")
printAllExercises(triceps)
print()

print("Forearms:")
printAllExercises(forearms)
print()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role":"user", "content":"Generate a 4-day workout plan hitting every muscle group using the following exercise lists: {chest} {back} {legs} {arms}. Make sure to include at least 5 workouts per day as well as the number of sets and reps for each workout"}
    ]
)

print(response.choices[0].message.content)