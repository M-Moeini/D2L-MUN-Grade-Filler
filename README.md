
# Automating Grades Entry on D2L Platform: Memorial University 

This Python script leverages Selenium to automate the meticulous task of entering grades, feedback, and extracting class lists within the D2L platform at Memorial University. Designed specifically for Teaching Assistants (TAs) and instructors.

## Key Features:

- **Automated Entry:** Streamlines the process of entering marks and feedback into assignment sections and grades into the platform's grading section.
- **Classlist Extraction:** Allows for easy extraction of class lists, simplifying administrative tasks.


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

    -1 If you want to to enter the assignment grades in assignment section, pass the excel path to `enter_assignment_marks` function with the course name and assignment name.(Inside `enter_assignment_marks` you can both work with `open_student_files` and  `open_student_names` functions depends on how you want to open the students works )

    -2 If you want to enter grades in grade section pass the excel path to `enter_grades` function  with course name and assesment name you want to grade.

    -3 If you want to get the class list as excel file you can use `get_classlist` function and pass the saving path for the output as well as the course name.

    - Check below to get familiar with `course_name`, `assignment_name` and `assesment_name`
    


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



## Note

- Ensure network stability and appropriate permissions before running the script to avoid interruptions in data entry.
- Adjusting the 'SLEEP' parameter significantly to a lower values might lead to incomplete page loading, causing issues for Selenium in locating elements.
- There is an exception handler for functions looking for student name and file name. If the function can not find the file or the student name it will goes to next iteration and will print the file or student name in the terminal. You should manually take care of these situatons. Usually happens with the names that have ' or -.
-You can modify the column order in the excel file but should also modify the code in the `read_data` fucntion.

## Disclaimer

- Use this script responsibly and in accordance with the policies of Memorial University. It's recommended to review the entered data for accuracy after the script execution.

## Contribution
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact
- **Mahdi Moeini**
  - **Email**: [mmoeini@mun.ca](mailto:mmoeini@mun.ca)
  - **LinkedIn**: [linkedin.com/in/mmoeini](https://linkedin.com/in/mmoeini)
  - **GitHub**: [m-moeini.github.io](https://m-moeini.github.io)
