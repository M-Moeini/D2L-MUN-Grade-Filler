
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

5. **Customize Course and Assignment:**
    Modify the `course_name` and `assignment_name` variables in the script to match the specific course and assignment you're grading. You can enter any part of the course name but for the assignment name it should be exactly what you see on the D2L.
    ![Courses](https://github.com/M-Moeini/D2L-MUN-Grade-Filler/blob/main/Images/Courses.png)

    ![Assignments](https://github.com/M-Moeini/D2L-MUN-Grade-Filler/blob/main/Images/Assignments.png)


6. **Run the Script:**
    Execute the script in a Python environment.

## Usage
- The script navigates through the D2L platform, accesses the specified course and assignment, maximizes student information, and automates the process of entering marks and feedback based on the provided Excel file.
## Functions and Their Usage

### `login(url, USERNAME, PASSWORD, SLEEP)`

- **Purpose:** Logs into the D2L platform with the provided URL, username, and password, pausing for the specified duration.
- **Parameters:**
    - `url`: URL of the D2L platform.
    - `USERNAME`: Username for login.
    - `PASSWORD`: Password for login.
    - `SLEEP`: Duration (in seconds) to wait after login.

### `open_course(name, SLEEP)`

- **Purpose:** Navigates to the specified course in the D2L platform, waiting for a specified duration.
- **Parameters:**
    - `name`: Name of the course to be accessed.
    - `SLEEP`: Duration (in seconds) to wait after accessing the course.

### `open_assignment_tab(SLEEP)`

- **Purpose:** Opens the assignment tab within the course, pausing for a specified duration.
- **Parameters:**
    - `SLEEP`: Duration (in seconds) to wait after opening the assignment tab.

### `open_assignment_dropdown(SLEEP, button_number)`

- **Purpose:** Opens a dropdown associated with a specific assignment, waiting for a specified duration.
- **Parameters:**
    - `SLEEP`: Duration (in seconds) to wait after opening the dropdown.
    - `button_number`: Number indicating which dropdown to open.

### `open_assignment_Section(name, SLEEP)`

- **Purpose:** Navigates to a specific section of the assignment, waiting for a specified duration.
- **Parameters:**
    - `name`: Name of the assignment section to be accessed.
    - `SLEEP`: Duration (in seconds) to wait after accessing the section.(No need to change)

### `maximize_student_number(SLEEP)`

- **Purpose:** Maximizes the number of displayed students for grading purposes, waiting for a specified duration.
- **Parameters:**
    - `SLEEP`: Duration (in seconds) to wait after maximizing student numbers.

### `open_student(names, marks, comments, SLEEP)`

- **Purpose:** Automates entering marks and comments for students based on provided data from an Excel file.
- **Parameters:**
    - `names`: List of student names.
    - `marks`: List of marks corresponding to each student.
    - `comments`: List of comments corresponding to each student.
    - `SLEEP`: Duration (in seconds) to wait after processing each student.

### `enter_mark(mark)`

- **Purpose:** Enters a mark into the D2L platform for a specific student.
- **Parameters:**
    - `mark`: The mark to be entered for a student.

### `save_draft(SLEEP)`

- **Purpose:** Saves the current grading progress as a draft, pausing for a specified duration.
- **Parameters:**
    - `SLEEP`: Duration (in seconds) to wait after saving the draft.

### `update(SLEEP)`

- **Purpose:** Updates the grading status, pausing for a specified duration.
- **Parameters:**
    - `SLEEP`: Duration (in seconds) to wait after updating.

### `back(SLEEP)`

- **Purpose:** Navigates back to the previous page or section, pausing for a specified duration.
- **Parameters:**
    - `SLEEP`: Duration (in seconds) to wait after navigating back.

### `enter_comments(comments, SLEEP)`

- **Purpose:** Enters comments/feedback for a specific student.
- **Parameters:**
    - `comments`: Comments or feedback for a student.
    - `SLEEP`: Duration (in seconds) to wait after entering comments.

## Note

- Ensure network stability and appropriate permissions before running the script to avoid interruptions in data entry.
## Disclaimer

- Use this script responsibly and in accordance with the policies of Memorial University. It's recommended to review the entered data for accuracy after the script execution.