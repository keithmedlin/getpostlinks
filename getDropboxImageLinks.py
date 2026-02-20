import argparse
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

parser = argparse.ArgumentParser(description="Extract raw image links from a Dropbox shared folder.")
parser.add_argument("url", nargs="?", help="Dropbox shared folder URL")
args = parser.parse_args()
url = args.url or input("Enter Dropbox shared folder URL: ")

# Regex to identify JUST the image files. This will pick up jpg, gif, png, but you can edit to your taste.
reg = re.compile(r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])\.(?:jpg|gif|png)')

urllist = []

# Selenium 4.6+ auto-manages chromedriver — no path or webdriver-manager needed.
browser = webdriver.Chrome()
browser.get(url)
time.sleep(1)

elem = browser.find_element(By.TAG_NAME, "body")

# If you have a massive listing of images, you may need to adjust this so that the page will scroll down enough.
# This is necessary since the dropbox site does progressive loading of images.
no_of_pagedowns = 25

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns -= 1

# instantiate the BeautifulSoup object to start parsing the html from dropbox
soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.quit()

# This line may need to be updated in the future if dropbox changes how they code the page.
# If you're getting back garbage results...check to ensure this makes sense still using Chrome Dev Tools
thumbs = soup.find_all("a", class_="sl-link sl-link--file")

for thumb in thumbs:
    urllist.append(str(thumb))

# just print out the actual link that we're looking for to create our spreadsheet.
for link in urllist:
    match = reg.search(link)
    if match:
        print(match.group() + "?raw=1")
