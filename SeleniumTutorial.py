from selenium import webdriver

browser = webdriver.Firefox() ## Must install geckodriver if using firefox browser

#Load a webpage
browser.get('https://www.google.com')

#Screenshot whatever is in the browser
browser.save_screenshot()

#Extract the links from page
browser.find_elements_by_*

#Clicks  ==> look up ActionChains() on selenium documentation
.click()