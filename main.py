from selenium import webdriver #instantiate the webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json


# enable the headless mode
options = Options()
options.add_argument('--headless=new')

# initialize a web driver to control Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
driver.get("http://selenium.dev")

# maxime the controlled browser window
driver.fullscreen_window()

# URL of the target page to scrape
url = 'https://www.reddit.com/r/technology/top/?t=week'
driver.get(url)

# scraping logic

# Get some basic info about subreddit
name = driver.find_element(By.XPATH, \
        "/html/body/shreddit-app/div/main/shreddit-async-loader[2]/div[2]/div[1]/div/div[2]/div[1]")\
        .get_attribute('innerText')

description = driver.find_element(By.CLASS_NAME, "text-left").get_attribute('innerText').strip()

members = driver.find_element(By.CSS_SELECTOR, "faceplate-number").get_attribute('innerText')

# Get Reddit's posts info
post_html_elements = driver.find_elements(By.TAG_NAME, "shreddit-post")

# Store it in a list
reddit_posts = []


for post_html_element in post_html_elements:
    post_text = post_html_element.get_attribute('innerText')
    # Split the post text into lines and remove any empty lines
    post_lines = [line.strip() for line in post_text.split('\n') if line.strip()]
    if len(post_lines) >= 5:
        post_dict = {
            "Author": post_lines[0],
            "Published date": post_lines[2],
            "Title": post_lines[3],
            "Topic": post_lines[4],
            "Link": post_lines[5]
        }
        # Append the dictionary to reddit_posts
        reddit_posts.append(post_dict)

# for post_html_element in post_html_elements:
#     post_text = post_html_element.get_attribute('innerText')
#     # Split the post text into lines and remove any empty lines
#     post_lines = [line.strip() for line in post_text.split('\n') if line.strip()]
#     if len(post_lines) >= 5:
#         post_dict = {
#             "Author": post_lines[0],
#             "Published date": post_lines[2],
#             "Title": post_lines[3],
#             "Topic": post_lines[4],
#             "Link": post_lines[5]
#         }
# #Append the dictionary to reddit_posts
# reddit_posts.append(post_dict)

# for post_html_element in post_html_elements:
#     post_text = post_html_element.get_attribute('innerText')
#     # Split the post text into lines and remove any empty lines
#     post_lines = [line.strip() for line in post_text.split('\n') if line.strip()]
#     # Append the list of lines to reddit_posts
#     reddit_posts.append(post_lines)

# for post_html_element in post_html_elements:
#     post_text = post_html_element.get_attribute('innerText')
#     # Append post_text directly to the list without a key
#     reddit_posts.append(post_text)

   
subreddit = {
    'name': name,
    'description': description,
    'members': members,
    'posts': reddit_posts
   }

# close the browser and free up the Selenium resources
driver.quit()


# export the scraped data to a JSON file
with open('subreddit.json', 'w', encoding='utf-8') as file:
    json.dump(subreddit, file, indent=4, ensure_ascii=False)

with open('subreddit.json', 'r') as file:
# Loading JSON data from the file into a Python object
  data = json.load(file)

 
