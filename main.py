from selenium import webdriver #instantiate the webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# enable the headless mode
options = Options()
options.add_argument('--headless=new')

# initialize a web driver to control Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
# maxime the controlled browser window
driver.fullscreen_window()

# the URL of the target page to scrape

url = 'https://www.reddit.com/r/technology/top/?t=week'

driver.get(url)
print("Hello")

# scraping logic...

name_element = driver.find_element(By.XPATH, "/html/body/shreddit-app/div/main/shreddit-async-loader[2]/div[2]/div[1]/div/div[2]/div[1]")

name = name_element.text

subreddit = {
    'name': name
}


print(subreddit)

# close the browser and free up the Selenium resources
driver.quit()