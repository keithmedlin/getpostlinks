from bs4 import BeautifulSoup
import requests
import cssutils
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# You'll need to install the Chrome Web Driver and point this line to it. https://chromedriver.chromium.org/downloads
browser = webdriver.Chrome('C:/Users/Keith/Documents/Python Scripts/chromedriver.exe')

# You'll need to update this each time you run the script for a new folder in a Dropbox Shared Folder.
url = "YOUR DROPBOX LINK HERE"

# Regex to identify JUST the image files. This will pick up jpg, gif, png, but you can edit to your taste.
reg = re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-]).(?:jpg|gif|png)')

# Instatiate the urllist object
urllist = []

browser.get(url)
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

# If you have a massive listing of images, you may need to adjust this so that the page will scroll down enough.
# This is necessary since the postimg site does progressive loading of images.
no_of_pagedowns = 25

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns-=1

# instantiate the BeautifulSoup object to start parsing the html from postimg
soup = BeautifulSoup(browser.page_source, 'html.parser')

# This line may need to be updated in the future if postimg.cc changes how they code the page.
# If you're getting back garbage results...check to ensure this makes sense still using Chrome Dev Tools
thumbs = soup.find_all("a", class_="sl-link sl-link--file")

# Get the appropriate element
for thumb in thumbs:
    urllist.append(str(thumb))

# just print out the actual link that we're looking for to create our spreadsheet.
for link in urllist:
  print(reg.search(link).group())
