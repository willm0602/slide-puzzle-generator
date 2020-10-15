from bs4 import BeautifulSoup
import requests, bs4, random, urllib
def writeFileImg(description,fileLocation):
    #!gets the image for the slide puzzle from user input
    #generates the URL for the location of the images
    url = 'https://www.google.com/search?q=THING&tbs=isz:m&tbm=isch&sxsrf=ACYBGNQxkxPep7vTH4u1sU4nq2edIhwoNw:1568229774233&source=lnt&sa=X&ved=0ahUKEwjy6vmUv8nkAhVMsZ4KHbtgBHwQpwUIIw&biw=1229&bih=603&dpr=1.56'
    url = url.replace('THING',description.replace(' ','+'))

    #gets the website data and parses it
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    #uncomment this if you want test.html to contain the html
    '''file = open('test.html','w').close()
    file = open('test.html','w')
    file.write(soup.prettify())'''

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
    return(getImg(images))
