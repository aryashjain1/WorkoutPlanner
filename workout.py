import requests
from bs4 import BeautifulSoup

"""r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
  
s = soup.find('div', class_='entry-content') 
print(type(s))
lines = s.find_all('p') 
  
for line in lines: 
    print(line.text)"""

# Making a GET request 
r = requests.get('https://www.menshealth.com/fitness/a19547186/best-chest-exercises/') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

c = soup.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

chest = c.find_all('h2')
chest = chest[5:-2] #removing irrelevant titles

print("All chest workouts:")
for line in chest:
    print(line.text)
print()

r2 = requests.get('https://www.menshealth.com/fitness/a29459907/best-leg-exercises/')

soup2 = BeautifulSoup(r2.content, 'html.parser')

l = soup2.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

legs = l.find_all('h2')
legs = legs[4:]

print("All leg workouts:")
for line in legs:
    print(line.text)
print()

r3 = requests.get('https://www.menshealth.com/fitness/a19545838/10-best-back-exercises/')

soup3 = BeautifulSoup(r3.content, 'html.parser')

b = soup3.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

back = b.find_all('h2')
back = back[9:-6]

print("All back workouts:")
for line in back:
    print(line.text)
print()

r4 = requests.get('https://www.menshealth.com/uk/building-muscle/a754655/16-best-exercises-for-bigger-arms/')

soup4 = BeautifulSoup(r4.content, 'html.parser')

a = soup4.find('div', class_ = 'article-body-content article-body standard-body-content css-yqyv4u ewisyje7')

arms = a.find_all('h2')
arms = arms[4:-5]
biceps = arms[:11]
triceps = arms[12:23]
forearms = arms[24:27]

print("All arms workouts: ")
print()
print("Biceps:")
for line in biceps:
    print(line.text)
print()

print("Triceps:")
for line in triceps:
    print(line.text)
print()

print("Forearms:")
for line in forearms:
    print(line.text)
print()