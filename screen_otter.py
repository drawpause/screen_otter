import sys, re
from selenium import webdriver

url = sys.argv[1]
filename = re.sub(r"[^\w\s]", ' ', url)
filename = re.sub(r"\s+", '-', filename) + '.png'
driver = webdriver.PhantomJS('phantomjs')
driver.set_window_size(1024, 768)
driver.get(str(url))
driver.save_screenshot(filename)
print('Saving to ' + str(filename))
driver.quit()
