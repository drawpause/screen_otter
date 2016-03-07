import sys, re
from selenium import webdriver

# Get the command line argument
url = sys.argv[1]

# Define protocols
http = 'http://'
https = 'https://'

# If url doesn't have the protocol prefix
if http or https not in url:
    url = http + url

# Make the filename nicer and strip special characters
filename = re.sub(r"[^\w\s]", ' ', url)
filename = re.sub(r"\s+", '-', filename) + '.png'

# Init PhantomJS
driver = webdriver.PhantomJS('phantomjs')
driver.set_window_size(1024, 768)
driver.get(str(url))
driver.save_screenshot(filename)
print('Saving to ' + str(filename))
driver.quit()
