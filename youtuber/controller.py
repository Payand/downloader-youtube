from youtuber import db
from youtuber.models import Info
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time







class Scraper:
    def __init__(self,url):
        self.url = url
    
    
    def web_progress(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.browser.maximize_window()
        cookies_btn=WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div/div[6]/div[1]/ytd-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string')))
        time.sleep(3)
        cookies_btn.click()
        
        time.sleep(5)
        duration= WebDriverWait(self.browser,20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'ytd-thumbnail-overlay-time-status-renderer')))
        videos =WebDriverWait(self.browser,20).until(EC.presence_of_all_elements_located((By.ID,'video-title-link')))
        # get first 8 videos
        for i  in range(0,8):
            time_duration = duration[i].text
            time.sleep(5)
            videos[i].click()
            time.sleep(10)
            title =WebDriverWait(self.browser,20).until(EC.presence_of_element_located
                                                        ((By.XPATH,'//*[@id="container"]/h1/yt-formatted-string'))).text
            date = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located
                                                         ((By.XPATH,'//*[@id="info-strings"]/yt-formatted-string'))).text
            url = self.browser.current_url
            info = Info(title = title,date=date ,duration=time_duration,url=url)
            db.session.add(info)
        db.session.commit()
        self.browser.back()
        time.sleep(10)
        self.browser.close()

            
            
            
        
