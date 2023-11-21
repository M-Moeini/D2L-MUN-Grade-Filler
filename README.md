
# Automating Marks and Feedback Entry on D2L Platform: Memorial University 

This Python script utilizes Selenium to automate the process of entering marks and feedback into the D2L platform at Memorial University. It's designed to streamline the workflow for TAs working on grading assignments.

## Requirments
- Python 3.x
- Selenium
- Chrome WebDriver
- Pandas
##  Setup Instructions
1. **Install Dependencies:**
    ```bash
    pip install selenium pandas
    ```

2. **Download Chrome WebDriver:**
    Download the Chrome WebDriver and ensure it's placed in your system's PATH or update the `driver` instantiation line in the script with the path to the WebDriver.(If you have already installed the chrome there is no need for that.)

3. **Excel File Format:**
    Prepare an Excel file with the required data columns (names, marks, comments, student IDs) for the assignments.

4. **Set Credentials:**
    Update the `username` and `password` variables in the script with your credentials for the Memorial University D2L platform.
    The `URL` should be the home URL of D2L. (No need to change)

5. **Customize Course and Assignment:**
    Modify the `course_name` and `assignment_name` variables in the script to match the specific course and assignment you're grading. You can enter any part of the course name but for the assignment name it should be exactly what you see on the D2L.


6. **Choose your goal:**
    - If you wanto to enter the assignment grades in assignment section, pass the excel path to `enter_assignment_marks` function with the course name and assignment name.(Inside `enter_assignment_marks` you can both work with `open_student_files` and  `open_student_names` functions depends on how you want to open the students works )
    - If you want to enter grades in grade section pass the excel path to `enter_grades` function  with course name and assesment name you want to grade.
    -Check below to get familiar with `course_name`, `assignment_name` and `assesment_name`
    ### Course name
    ![Courses](https://github.com/M-Moeini/D2L-MUN-Grade-Filler/blob/main/Images/Courses.png)
    ### Assignment name
    ![Assignments](https://github.com/M-Moeini/D2L-MUN-Grade-Filler/blob/main/Images/Assignments.png)
    ### Assesment name
    ![Assesment](https://github.com/M-Moeini/D2L-MUN-Grade-Filler/blob/main/Images/Assesment.png)

6. **Run the Script:**
    Execute the script in a Python environment.

## Usage
- The script navigates through the D2L platform, accesses the specified course and assignment, maximizes student information, and automates the process of entering marks and feedback based on the provided Excel file.


## Functions and Their Usage
1. **login(url, USERNAME, PASSWORD, SLEEP):**
    - Logs into a specified URL using provided username and password.
    - Parameters:
        - `url`: URL to login.
        - `USERNAME`: Username for login.
        - `PASSWORD`: Password for login.
        - `SLEEP`: Time delay in seconds.

2. **open_course(name, SLEEP):**
    - Opens a specific course.
    - Parameters:
        - `name`: Name of the course to be opened.
        - `SLEEP`: Time delay in seconds.

3. **open_assignment_tab(SLEEP):**
    - Opens the assignment tab.
    - Parameters:
        - `SLEEP`: Time delay in seconds.

4. **open_grades_tab(SLEEP, grade_tab_number):**
    - Opens the grades tab.
    - Parameters:
        - `SLEEP`: Time delay in seconds.
        - `grade_tab_number`: Number corresponding to the grades tab.

5. **open_assessment_dropdown(SLEEP, button_number):**
    - Opens a dropdown for assessments.
    - Parameters:
        - `SLEEP`: Time delay in seconds.
        - `button_number`: Number corresponding to the dropdown button.

6. **open_assignment_section(name, SLEEP):**
    - Opens a particular assignment section.
    - Parameters:
        - `name`: Name of the assignment section.
        - `SLEEP`: Time delay in seconds.

7. **maximize_student_number(SLEEP):**
    - Maximizes the number of displayed students.
    - Parameters:
        - `SLEEP`: Time delay in seconds.

8. **open_student_names(names, marks, comments, SLEEP):**
    - Opens student details for grading.
    - Parameters:
        - `names`: List of student names.
        - `marks`: List of marks.
        - `comments`: List of comments.
        - `SLEEP`: Time delay in seconds.

9. **open_student_files(student_ids, marks, comments, SLEEP):**
    - Opens files submitted by students.
    - Parameters:
        - `student_ids`: List of student IDs.
        - `marks`: List of marks.
        - `comments`: List of comments.
        - `SLEEP`: Time delay in seconds.

10. **enter_mark(mark):**
    - Enters a specific mark.
    - Parameters:
        - `mark`: The mark to be entered.

11. **save_draft(SLEEP):**
    - Saves the current draft.
    - Parameters:
        - `SLEEP`: Time delay in seconds.

12. **update(SLEEP):**
    - Updates the current status.
    - Parameters:
        - `SLEEP`: Time delay in seconds.

13. **back(SLEEP):**
    - Navigates back to the previous screen.
    - Parameters:
        - `SLEEP`: Time delay in seconds.

14. **enter_comments(comments, SLEEP):**
    - Enters comments for evaluation.
    - Parameters:
        - `comments`: Comments to be entered.
        - `SLEEP`: Time delay in seconds.

15. **select_assessment(name, SLEEP):**
    - Selects a specific assessment.
    - Parameters:
        - `name`: Name of the assessment.
        - `SLEEP`: Time delay in seconds.

16. **enter_grade(names, marks):**
    - Enters grades for specific students.
    - Parameters:
        - `names`: List of student names.
        - `marks`: List of marks.

17. **save_and_close(SLEEP):**
    - Saves and closes the current status.
    - Parameters:
        - `SLEEP`: Time delay in seconds.

18. **enter_grades(data_path, course_name, assessment_name):**
    - A higher-level function to enter grades for a specific assessment.
    - Parameters:
        - `data_path`: Path to the data file.
        - `course_name`: Name of the course.
        - `assessment_name`: Name of the assessment.

19. **enter_assignment_marks(data_path, course_name, assignment_name):**
    - A function to enter marks for a specific assignment.
    - Parameters:
        - `data_path`: Path to the data file.
        - `course_name`: Name of the course.
        - `assignment_name`: Name of the assignment.

20. **read_data(PATH):**
    - Reads data from an Excel file.
    - Parameters:
        - `PATH`: Path to the Excel file.


## Note

- Ensure network stability and appropriate permissions before running the script to avoid interruptions in data entry.
- Adjusting the 'SLEEP' parameter significantly to a lower values might lead to incomplete page loading, causing issues for Selenium in locating elements.

## Disclaimer

- Use this script responsibly and in accordance with the policies of Memorial University. It's recommended to review the entered data for accuracy after the script execution.