from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.remote_connection import LOGGER
import requests
import logging
import os



def create_folder_save_Episode(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_path}' already exists.")
        pass
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        quit()

    with open(f'{folder_path}/{filename}-{split_name[2]}.mp4', "wb") as f:
        f.write(response.content)



LOGGER.setLevel(logging.ERROR)


HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36"}

options = Options()
options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

anime_name = input('name: ').replace(' ','-')
session = input('which seasion: ')
Sepisodes = int(input('start: '))
Eepisodes = int(input('end: '))

for i in range(Sepisodes, Eepisodes+1):

    Link_name = f'{anime_name}/staffel-{session}/episode-{i}'
    split_name = Link_name.split('/')
    filename = split_name[0]
    try :
        response = requests.get(f'https://aniworld.to/anime/stream/{Link_name}',headers=HEADER)
    except:
        print('ERROR anime not found')
        quit()
    
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a', class_='watchEpisode', attrs={'class': 'icon Vidoza'})
    vidoza_links = [link['href'] for link in links]
    readylink = f'{Link_name} : https://aniworld.to{vidoza_links[2]}'
    download_rlink = f'https://aniworld.to{vidoza_links[2]}'
#download the anime
    driver.get(download_rlink)
    video_element = driver.find_element(By.TAG_NAME, 'video')
    video_source_url = video_element.get_attribute("src")

    response = requests.get(video_source_url)
    print(f'{Link_name} is getting downloaded')



    create_folder_save_Episode(f'D:/animes/{anime_name}')



# Close the WebDriver session after processing all episodes
driver.quit()

