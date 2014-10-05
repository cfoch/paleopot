from urllib import urlopen
from bs4 import BeautifulSoup

MIX = -1
LEAVES = 0
LEGUMES = 1
FRUITS = 2

class FoodCrawler():
    def __init__(self):
        self.main_url = 'http://en.wikipedia.org'

    def listFruits(self, url):
        soup = self.makeSoup(url)
        tags = soup.findAll('div')
        # TODO: Complete me!

    def listLeafyVeggies(self, url):
        soup = self.makeSoup(url)
        tags = soup.findAll('td')

        veggies = []
        for i in range(1, len(tags), 3):
            name = tags[i].string
            url_tag = str(tags[i - 1])
            link = ''
            if url_tag is not None:
                soup_url = BeautifulSoup(url_tag)
                a = soup_url.findAll('a', href=True)
                link = self.main_url + a[0]['href']
            if name is not None:
                food = self.makeFood(name, url=link, category=MIX)
                veggies.append(food)
        return veggies

    def makeFood(self, name, url='', description='', category=''):
        food = {
            "url": url,
            "name": name.lower(),
            "description": description,
            "category": category
        }
        return food

    def makeSoup(self, url):
        page = urlopen(url)
        contents = page.read()
        return BeautifulSoup(contents)
        

crawler = FoodCrawler()
leafyVeggiesURL = "htmls/leafyVegetables.html"
frutisURL = "htmls/fruits.html"

print crawler.listLeafyVeggies(leafyVeggiesURL)

