from bs4 import BeautifulSoup
from webbot import Browser
import csv

# login information
user = "thiswontwork"
password = "thiswontwork"

# goes to the page and logs in
web = Browser()
web.go_to('https://www.zumostraining.co.uk/Login.aspx')
web.type(user)
web.press(web.Key.TAB)
web.type(thiswontwork)
web.click('Login')
web.click('Ignore')
web.go_to('https://www.zumostraining.co.uk/Zumos/Klik.aspx')

# passes the source to BeautifulSoup
content = web.get_page_source()
soup = BeautifulSoup(content,'lxml')

# selects the elements with the attribute type set as an image
videos = []
videos = soup.findAll("input",{'class' : 'slick-slide'}) # videos is a list

# prints length of the array. Used for testing
print("Length:")
print(len(videos))

for video in videos:
    #concatenate to link and print for output
    out = 'https://www.youtube.com/watch?v='+video['youtubeid']
    #save to file
    # writer.writerows(out)
    # print to confirm it worked
    print(out)