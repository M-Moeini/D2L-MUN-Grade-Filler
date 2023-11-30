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

def open_grades_tab(SLEEP,grade_tab_number):
    tabs = (driver.find_element(By.CSS_SELECTOR, 'd2l-dropdown-menu[opened]')
            .find_elements(By.CSS_SELECTOR, 'd2l-menu-item-link')
            
)
    grades = tabs[grade_tab_number].shadow_root.find_element(By.CSS_SELECTOR,"a")

    grades.send_keys(Keys.ENTER)
    time.sleep(SLEEP)

def open_assesment_dropdown(SLEEP,button_number): 
    outer_div = driver.find_elements(By.CSS_SELECTOR, '.d2l-navigation-s-item')
    dropdown = outer_div[button_number-1].find_element(By.CSS_SELECTOR,'.d2l-navigation-s-group')
    dropdown.click()
    time.sleep(SLEEP)

def open_assignment_section(name,SLEEP):
    assignment = (driver.find_element(By.ID,'z_d')
                  .find_element(By.CSS_SELECTOR, 'tbody')
                  .find_elements(By.CSS_SELECTOR, 'tr')
   
    )
    for i in range(3,len(assignment)):
       if name in assignment[i].find_element(By.CSS_SELECTOR,'a').get_attribute('title'):
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
    time.sleep(SLEEP/2)

def open_student_names(names,marks,comments,SLEEP):
        
    for i in  range(len(names)):
        time.sleep(SLEEP/2)
        words = names[i].split()
        reversed_name = ' '.join(words[-1:] + words[0:len(words)-1])
        # formatted_name = reversed_name.replace(' ', ', ', 1)
        # title_text = formatted_name
        title_text = reversed_name
        try:
            student = driver.find_element(By.XPATH, f"//a[contains(translate(@title, ',', ''), '{title_text}')]")
            student.click()
            time.sleep(SLEEP)
            enter_mark(marks[i])
            enter_comments(comments[i], 5)
            save_draft(5)
            back(5)
            index = i+1
            print(str(index) + '-'+f'Student {names[i]} is done.')

        except NoSuchElementException:
            index = i+1
            print(str(index) + '-'+f"Student '{title_text}' not found. Moving to the next student.")
            continue

        except Exception as e:
            index = i+1
            print(str(index) + '-'+f"An unexpected exception occurred for student '{title_text}'. Moving to the next student.")
            continue
        
    time.sleep(SLEEP)


#open based on file name
#Here as an example the file name is 'student_id.zip' you can modified it per your preferance.
def open_student_files(studen_ids,marks,comments,SLEEP):
    
    for j in range (len(studen_ids)):
        file_name = f"Open {studen_ids[j]}.zip"
        try:
            file = driver.find_element(By.CSS_SELECTOR, f"[title=\"{file_name}\"]").click()
            time.sleep(SLEEP)
            enter_mark(marks[j])
            enter_comments(comments[j],5)
            # update(5)
            save_draft(5)
            back(5)
            index = j+1
            print(str(index) + '-'+ f"file '{file_name}' is done.")
        except NoSuchElementException:
            print(str(index) + '-'+f"file '{file_name}' not found. Moving to the next student.")
            continue

        except Exception as e:
            print(str(index) + '-'+f"An unexpected exception occurred for file '{file_name}'. Moving to the next student.")
            continue
        
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
    input.send_keys(int(mark))

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
    feedback.send_keys(str(comments))
    time.sleep(SLEEP)
    driver.switch_to.default_content()

def select_assesment(name,SLEEP):
    table_rows = (driver.find_element(By.ID, 'z_bi')
        .find_element(By.CSS_SELECTOR,'tbody')
        .find_elements(By.CSS_SELECTOR,'tr')
)
    second_header_flag = False
    table_headers = table_rows[1].find_elements(By.CSS_SELECTOR,'th')
    for i in range(len(table_headers)):
        assesment_name = table_headers[i].find_element(By.CSS_SELECTOR,'d2l-table-col-sort-button').text
        if name == assesment_name:
            l=i
            break
        elif(i==len(table_headers)-1):
            second_header_flag = True
            table_headers_secondary = table_rows[0].find_elements(By.CSS_SELECTOR,'th')
            for k in range(len(table_headers_secondary)):
                try:
                    if table_headers_secondary[k].find_element(By.CSS_SELECTOR, 'd2l-table-col-sort-button').is_displayed():
                        assesment_name = table_headers_secondary[k].find_element(By.CSS_SELECTOR, 'd2l-table-col-sort-button').text
                        if name == assesment_name:
                            l = k
                            break
                        else:
                            print("Assessment not found!")
                except NoSuchElementException:
                    continue

    if(second_header_flag):
        dropdwon = (table_headers_secondary[l].find_element(By.CSS_SELECTOR,'d2l-dropdown-context-menu')
            .shadow_root.find_element(By.CSS_SELECTOR,'d2l-button-icon')
            .shadow_root.find_element(By.CSS_SELECTOR,'button')
            )
        dropdwon.click()
        
        options = ( table_headers_secondary[l].find_element(By.CSS_SELECTOR, 'd2l-dropdown-context-menu')
                    .find_element(By.CSS_SELECTOR,'d2l-dropdown-menu')
                    .find_element(By.CSS_SELECTOR,'d2l-menu')
                    .find_elements(By.CSS_SELECTOR,'d2l-menu-item')
        )

        for i in range(len(options)):
            if(options[i].get_attribute('aria-label') == 'Enter Grades'):
                index = i
                break
        enter_grades = options[index]
        enter_grades.click()


    else:
        dropdwon = (table_headers[l].find_element(By.CSS_SELECTOR,'d2l-dropdown-context-menu')
                    .shadow_root.find_element(By.CSS_SELECTOR,'d2l-button-icon')
                    .shadow_root.find_element(By.CSS_SELECTOR,'button')
                    )
        dropdwon.click()

        options = ( table_headers[l].find_element(By.CSS_SELECTOR, 'd2l-dropdown-context-menu')
                    .find_element(By.CSS_SELECTOR,'d2l-dropdown-menu')
                    .find_element(By.CSS_SELECTOR,'d2l-menu')
                    .find_elements(By.CSS_SELECTOR,'d2l-menu-item')
        )

        for i in range(len(options)):
            if(options[i].get_attribute('aria-label') == 'Enter Grades'):
                index = i
                break
        enter_grades = options[index]
        enter_grades.click()



        

    time.sleep(SLEEP)


def enter_grade(names,marks):
    maximize_student_number(2)
    for i in  range(len(names)):
        
        try:
            time.sleep(1)
            title_text = 'Grade for ' + names[i]
            grade = (driver.find_element(By.XPATH, f"//d2l-input-number[contains(@title, '{title_text}')]")
                        .shadow_root.find_element(By.CSS_SELECTOR,'d2l-input-text')
                        .shadow_root.find_element(By.CLASS_NAME,'d2l-input-text-container')
                        .find_element(By.CSS_SELECTOR,'input'))
            mark = str(marks[i])    
            grade.clear()
            grade.send_keys(mark)
            index = i+1
            print(str(index) + '-'+ f"Student '{names[i]}' is done.")
            # if(i%5==0):
            #     save_grades(5)
        except NoSuchElementException:
            index = i+1
            print(str(index) + '-'+ f"Student '{names[i]}' not found. Moving to the next student.")
            continue

        except Exception as e:
            index = i+1
            print(str(index) + '-'+ f"An unexpected exception occurred for student '{names[i]}'. Moving to the next student.")
            continue
    save_and_close(5)

def save_grades(SLEEP):
    save_b = (driver.find_element(By.CSS_SELECTOR,'d2l-floating-buttons')
                        .find_element(By.XPATH,"//button[text()='Save']"))   
    save_b.click()
    time.sleep(SLEEP/3)
    yes = driver.find_element(By.XPATH,"//button[text()='Yes']")
    yes.click()
    time.sleep(SLEEP)

        
def save_and_close(SLEEP):
    save_and_close_b = (driver.find_element(By.CSS_SELECTOR,'d2l-floating-buttons')
                        .find_element(By.XPATH,"//button[text()='Save and Close']"))   
    save_and_close_b.click()
    time.sleep(SLEEP/3)
    yes = driver.find_element(By.XPATH,"//button[text()='Yes']")
    yes.click()
    time.sleep(SLEEP)

def enter_grades(data_path,course_name,assement_name):
    names,marks,comments,student_ids = read_data(data_path)
    open_course(course_name,1)
    open_assesment_dropdown(1,4)
    open_grades_tab(5,1)
    select_assesment(assement_name,1)
    enter_grade(names,marks)


def enter_assignment_marks(data_path,course_name,assignment_name):
    # names,marks,comments,student_ids = read_data(data_path)
    names,marks,comments,student_ids = read_data(data_path)
    # comments = ''
    open_course(course_name,1)
    open_assesment_dropdown(1,4)
    open_assignment_tab(5)
    open_assignment_section(assignment_name,1)
    open_student_names(names,marks,comments,5)
    # open_student_files(student_ids,marks,comments,5)

def read_data(PATH):
    data = pd.read_excel(PATH)
    data = data.iloc[:,:].reset_index(drop=True)
    names = data.iloc[:, 0]
    marks = data.iloc[:,8]
    comments = data.iloc[:,8]
    studen_ids = data.iloc[:,8]
    return names,marks,comments,studen_ids

def get_classlist(course_name,save_path):
    df = pd.DataFrame(columns=['fullnames'])
    open_course(course_name,1)
    open_assesment_dropdown(1,4)
    open_grades_tab(5,1)
        
    choices = (driver.find_element(By.CSS_SELECTOR,'div.d2l-grid-container')
                .find_elements(By.CSS_SELECTOR,'div.d2l-select-container')
    )
    options = choices[-1].find_element(By.CLASS_NAME, 'd2l-select').find_elements(By.CSS_SELECTOR,'option')        
    options[-1].click()
    time.sleep(5/2)
    rows = (driver.find_element(By.ID,'z_bi')
            .find_element(By.CSS_SELECTOR,'tbody')
            .find_elements(By.CSS_SELECTOR,'tr')
            )
    for i in range(2,len(rows)):
        rows = (driver.find_element(By.ID,'z_bi')
            .find_element(By.CSS_SELECTOR,'tbody')
            .find_elements(By.CSS_SELECTOR,'tr')
            )
        name = rows[i].find_element(By.CSS_SELECTOR,'th').find_element(By.CSS_SELECTOR,'d2l-dropdown-context-menu').get_attribute('text')
        name = name.replace("Actions for ", "")
        df.loc[i, 'fullnames'] = name

    df.to_excel(save_path, index=False)

    

username = ''
password = ''
course_name = ''
assignment_name = ''
assement_name = ''
url = "https://login.mun.ca/cas/login?service=https%3a%2f%2fonline.mun.ca%2fd2l%2fcustom%2fcas%3ftarget%3d%252fd2l%252fhome"
file_path = ""
save_path = ""

edge_options = webdriver.ChromeOptions()
edge_options.headless = True
edge_options.add_argument("--start-fullscreen")
driver = webdriver.Chrome(options=edge_options)

login(url,username,password,1)


enter_grades(file_path,course_name,assement_name)
# enter_assignment_marks(file_path,course_name,assignment_name)
# get_classlist(course_name,save_path,5)




    

driver.quit()