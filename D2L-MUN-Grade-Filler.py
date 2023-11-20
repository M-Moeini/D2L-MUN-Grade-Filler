from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def login(url,USERNAME,PASSWROD):
    driver.get(url)
    username = driver.find_element(By.ID, "username") 
    password = driver.find_element(By.ID, "password") 
    username.send_keys(USERNAME)
    password.send_keys(PASSWROD)
    password.send_keys(Keys.RETURN)  



username = "mmoeini"
password = "SSantajen146"
mark = ''
student_id = 202293111
title = f"Open {student_id}.zip"
url = "https://login.mun.ca/cas/login?service=https%3a%2f%2fonline.mun.ca%2fd2l%2fcustom%2fcas%3ftarget%3d%252fd2l%252fhome"
edge_options = webdriver.ChromeOptions()
edge_options.headless = True
edge_options.add_argument("--start-fullscreen")








driver = webdriver.Chrome(options=edge_options)

login(url,username,password)

# driver.find_element(By.CSS_SELECTOR, f"[title=\"{title}\"]").click()
# time.sleep(6)



# input= (driver.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-page')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'consistent-evaluation-right-panel')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'consistent-evaluation-right-panel-evaluation')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-right-panel-grade-result')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-labs-d2l-grade-result-presentational')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-grade-result-numeric-score')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-input-number')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-input-text')
#                 .shadow_root.find_element(By.CLASS_NAME,'d2l-input')               
# )
# save_draft = (driver.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-page')
#                 .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-footer')
#                 .shadow_root.find_element(By.ID, 'consistent-evaluation-footer-save-draft')
#                 )
# time.sleep(1)
# input.clear()
# input.send_keys(mark)
# time.sleep(2)
# save_draft.click()
# time.sleep(10)

driver.quit()