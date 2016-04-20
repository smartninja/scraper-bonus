import BeautifulSoup
import urllib2
from model import Person
from util import create_csv_file

url = 'https://scrapebook22.appspot.com/'

html = urllib2.urlopen(url).read()

soup = BeautifulSoup.BeautifulSoup(html)

print soup.html.head.title.string  # should be: Scrapebook | by SmartNinja

persons = []

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urllib2.urlopen(person_url).read()
        person_soup = BeautifulSoup.BeautifulSoup(person_html)

        email = person_soup.find("span", attrs={"class": "email"}).string
        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        city = person_soup.find("span", attrs={"data-city": True}).string

        first_name, last_name = name.split(" ")

        person = Person(first_name=first_name, last_name=last_name, email=email, city=city)
        persons.append(person)

        print(person.email)

csv_question = raw_input("Do you want to save data into a CSV file? (yes/no) ")

if csv_question == "yes":
    create_csv_file(persons)

print("Thanks for using this program :)")
