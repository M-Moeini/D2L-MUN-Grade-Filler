from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd


def login(url,USERNAME,PASSWROD,SLEEP):
    driver.get(url)
    username = driver.find_element(By.ID, "username") 
    password = driver.find_element(By.ID, "password") 
    username.send_keys(USERNAME)
    password.send_keys(PASSWROD)
    password.send_keys(Keys.RETURN)  
    time.sleep(SLEEP)

def open_course(name,SLEEP):
    courses = (driver.find_element(By.CSS_SELECTOR, 'd2l-my-courses')
                .shadow_root.find_element(By.CSS_SELECTOR,'d2l-my-courses-container')
                .shadow_root.find_element(By.CSS_SELECTOR,'d2l-my-courses-content')
                .shadow_root.find_element(By.CSS_SELECTOR,'d2l-my-courses-card-grid')
                .shadow_root.find_elements(By.CSS_SELECTOR,'d2l-enrollment-card')               
    )
    for i in range(len(courses)):
        course_name = courses[i].shadow_root.find_element(By.CSS_SELECTOR,'d2l-card').text
        if name in course_name:
            j = i
            break
        elif i ==len(course_name)-1:
            print("Course name does not match") 

    courses[j].click()
    time.sleep(SLEEP)

def open_assignment_tab(SLEEP):
    assignment = (driver.find_element(By.CSS_SELECTOR, 'd2l-dropdown-menu[opened]')
                .find_element(By.CSS_SELECTOR, 'd2l-menu-item-link')
                .shadow_root.find_element(By.CSS_SELECTOR,"a")
    )
    assignment.send_keys(Keys.ENTER)
    time.sleep(SLEEP)

def open_assignment_dropdown(SLEEP,button_number): 
    outer_div = driver.find_elements(By.CSS_SELECTOR, '.d2l-navigation-s-item')
    dropdown = outer_div[button_number-1].find_element(By.CSS_SELECTOR,'.d2l-navigation-s-group')
    dropdown.click()
    time.sleep(SLEEP)

def open_assignment_Section(name,SLEEP):
    assignment = (driver.find_element(By.ID,'z_d')
                  .find_element(By.CSS_SELECTOR, 'tbody')
                  .find_elements(By.CSS_SELECTOR, 'tr')
   
    )
    print(len(assignment))
    for i in range(3,len(assignment)):
       if name in assignment[3].find_element(By.CSS_SELECTOR,'a').get_attribute('title'):
            j = i
            break
    assignment[j].find_element(By.CSS_SELECTOR,'a').click()
    time.sleep(SLEEP)


def maximize_student_number(SLEEP):
    
    options = (driver.find_element(By.CSS_SELECTOR,'div.d2l-grid-container')
              .find_element(By.CSS_SELECTOR,'div.d2l-select-container')
              .find_element(By.CLASS_NAME, 'd2l-select')
              .find_elements(By.CSS_SELECTOR,'option')
    )
    options[-1].click()
    time.sleep(SLEEP)
    print(options[1].text,"hi")

def open_student(names,marks,comments,SLEEP):

    for j in range (len(names)):
        student = (driver.find_element(By.CSS_SELECTOR,'d2l-table-wrapper')
            .find_element(By.CSS_SELECTOR,'tbody')
            .find_elements(By.CLASS_NAME,'d_ggl2')

        )
        print(j)
        for i in range(len(student)):
            student = (driver.find_element(By.CSS_SELECTOR,'d2l-table-wrapper')
            .find_element(By.CSS_SELECTOR,'tbody')
            .find_elements(By.CLASS_NAME,'d_ggl2')

            )
            print(i)
            s_name = (student[i].find_element(By.CSS_SELECTOR,'th')
                        .find_element(By.CSS_SELECTOR,'table')
                        .find_element(By.CSS_SELECTOR,'td')
                        .find_element(By.CSS_SELECTOR,'a')
            )
            print(names[j],s_name.text,"hi")
            if names[j] in s_name.text:
                s_name.click()
                time.sleep(SLEEP)
                enter_mark(marks[j])
                enter_comments(comments[j],5)
                update(5)
                back(5)
                break
            elif(i==len(student)-1):
                print("Name not found")
        
    time.sleep(SLEEP)

def enter_mark(mark):
    
    input= (driver.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation')
                    .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-page')
                    .shadow_root.find_element(By.CSS_SELECTOR,'consistent-evaluation-right-panel')
                    .shadow_root.find_element(By.CSS_SELECTOR,'consistent-evaluation-right-panel-evaluation')
                    .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-right-panel-grade-result')
                    .shadow_root.find_element(By.CSS_SELECTOR,'d2l-labs-d2l-grade-result-presentational')
                    .shadow_root.find_element(By.CSS_SELECTOR,'d2l-grade-result-numeric-score')
                    .shadow_root.find_element(By.CSS_SELECTOR,'d2l-input-number')
                    .shadow_root.find_element(By.CSS_SELECTOR,'d2l-input-text')
                    .shadow_root.find_element(By.CLASS_NAME,'d2l-input')               
    )
    input.clear()
    input.send_keys(mark)

def save_draft(SLEEP):
    save_draft = (driver.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation')
                .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-page')
                .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-footer')
                .shadow_root.find_element(By.ID, 'consistent-evaluation-footer-save-draft')
                )
    save_draft.click()
    time.sleep(SLEEP)

def update(SLEEP):
    update = (driver.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation')
            .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-page')
            .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-footer')
            .shadow_root.find_element(By.ID, 'consistent-evaluation-footer-update')
                )
    update.click()
    time.sleep(SLEEP)
def back(SLEEP):
    back = (driver.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation')
            .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-page')
            .shadow_root.find_element(By.CSS_SELECTOR,'d2l-consistent-evaluation-nav-bar')
            .shadow_root.find_element(By.CSS_SELECTOR,'d2l-navigation-link-back')
            .shadow_root.find_element(By.CSS_SELECTOR,'d2l-navigation-link-icon')
            .shadow_root.find_element(By.CSS_SELECTOR,'a')   
    )
    back.send_keys(Keys.ENTER)
    time.sleep(SLEEP)

def enter_comments(comments,SLEEP):
    iframe = (
        driver.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation')
        .shadow_root.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation-page')
        .shadow_root.find_element(By.CSS_SELECTOR, 'consistent-evaluation-right-panel')
        .shadow_root.find_element(By.CSS_SELECTOR, 'consistent-evaluation-right-panel-evaluation')
        .shadow_root.find_element(By.CSS_SELECTOR, 'd2l-consistent-evaluation-right-panel-feedback')
        .shadow_root.find_element(By.CSS_SELECTOR, 'd2l-htmleditor')
        .shadow_root.find_element(By.ID, 'd2l-uid-35_ifr')
    )
    driver.switch_to.frame(iframe)
    feedback = driver.find_element(By.TAG_NAME, 'body')
    feedback.clear()
    feedback.send_keys(comments)
    time.sleep(SLEEP)
    driver.switch_to.default_content()

#only for 9818 course
#open based on file name
def open_student(studen_ids,marks,comments,SLEEP):
    
    for j in range (len(studen_ids)):
        file_name = f"Open {studen_ids[j]}.zip"
        file = driver.find_element(By.CSS_SELECTOR, f"[title=\"{file_name}\"]").click()
        time.sleep(SLEEP)
        enter_mark(marks[j])
        enter_comments(comments[j],5)
        update(5)
        back(5)
        
    time.sleep(SLEEP)


        
        
    

username = "mmoeini"
password = "SSantajen146"
course_name = 'Computer Software'
assignment_name = 'assignment 0'
student_id = 202293111
title = f"Open {student_id}.zip"
url = "https://login.mun.ca/cas/login?service=https%3a%2f%2fonline.mun.ca%2fd2l%2fcustom%2fcas%3ftarget%3d%252fd2l%252fhome"
edge_options = webdriver.ChromeOptions()
edge_options.headless = True
edge_options.add_argument("--start-fullscreen")

driver = webdriver.Chrome(options=edge_options)
file_path = "C:\\Users\\Mahdi\\Desktop\\Names.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)
names = data.iloc[:, 0]
marks = data.iloc[:,1]
comments = data.iloc[:,2]
studen_ids = data.iloc[:,3]
login(url,username,password,1)
open_course(course_name,1)
open_assignment_dropdown(1,4)
open_assignment_tab(5)
open_assignment_Section(assignment_name,1)
maximize_student_number(5)
# open_student(names,marks,comments,5)
open_student(studen_ids,marks,comments,5)


# driver.find_element(By.CSS_SELECTOR, f"[title=\"{title}\"]").click()
# time.sleep(6)








# time.sleep(1)
# input.clear()
# input.send_keys(mark)
# time.sleep(2)
# save_draft.click()
# time.sleep(10)

driver.quit()