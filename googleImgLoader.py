from bs4 import BeautifulSoup
import requests, bs4, random, urllib
def writeFileImg(description,fileLocation):
    #!gets the image for the slide puzzle from user input
    #generates the URL for the location of the images
    url = 'https://www.google.com/search?tbm=isch&q=THING'
    url = url.replace('THING',description.replace(' ','+'))

    #gets the website data and parses it
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    #gets each element
    images = soup.find_all('img',None,True)
    
    #picks a random URL to get image
    def getImg(urls):
        try:
            choice = random.choice(urls)
            img = choice['src']
            img = requests.get(img).content
            file = open(fileLocation,'wb')
            file.write(img)
            file.close()    
        except:
            getImg(urls)
    getImg(images)
