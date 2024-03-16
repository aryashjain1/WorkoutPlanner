import random
import requests
from bs4 import BeautifulSoup

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
        print(line.text)

def printAllArmExercises(part):
    for line in part:
        print(line)


# Making a GET request 
r = requests.get('https://www.menshealth.com/fitness/a19547186/best-chest-exercises/') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

c = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

chest = c.find_all('h2')
chest = chest[5:-2] #removing irrelevant titles

print("All chest workouts:")
printAllExercises(chest)
print()

r = requests.get('https://www.menshealth.com/fitness/a29459907/best-leg-exercises/')

soup = BeautifulSoup(r.content, 'html.parser')

l = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

legs = l.find_all('h2')
legs = legs[4:]

print("All leg workouts:")
printAllExercises(legs)
print()

r = requests.get('https://www.menshealth.com/fitness/a19545838/10-best-back-exercises/')

soup = BeautifulSoup(r.content, 'html.parser')

b = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

back = b.find_all('h2')
back = back[9:-6]

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
printAllArmExercises(biceps)
print()

print("Triceps:")
printAllArmExercises(triceps)
print()

print("Forearms:")
printAllArmExercises(forearms)
print()

num_chest = 1
num_chest_upper = 2
num_back = 4
num_quads = 3
num_hamstrings = 3
num_biceps = 2
num_triceps = 2
num_forearms = 1

w_chest = getRandom(chest, num_chest)
w_upper_chest = getRandom(chest, num_chest_upper)
w_back = getRandom(back, num_back)
w_quads = getRandom(legs, num_quads)
w_hamstrings = getRandom(legs, num_hamstrings)
w_biceps= getRandom(biceps, num_biceps)
w_triceps = getRandom(triceps, num_triceps)
w_forearms = getRandom(forearms, num_forearms)

print("Workout split for the week: ")
print("Chest: ")
for line in w_chest:
    print(line.text)
print("Upper Chest:")
for line in w_upper_chest:
    print(line.text)
print()
print("Back:")
for line in w_back:
    print(line.text)
print()
print("Legs:")
print("Quads:")
for line in w_quads:
    print(line.text)
print("Hamstrings:")
for line in w_hamstrings:
    print(line.text)
print()
print("Arms:")
print("Biceps:")
for line in w_biceps:
    print(line)
print("Triceps:")
for line in w_triceps:
    print(line)
print("Forearms:")
for line in w_forearms:
    print(line)