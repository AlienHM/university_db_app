# Student and Teacher Management System

This project is a web application built with Flask that allows you to manage student and teacher data. The application supports adding new students and teachers, filtering data based on search queries, and resetting the database to its initial state.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Features

- Add new students and teachers with their details.
- View lists of students and teachers.
- Filter data based on search queries.
- Reset the database to its initial state with predefined majors.
- Uses Redis for data storage.

## Technologies Used

- Python
- Flask
- Redis
- HTML
- CSS
- JavaScript

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/student-teacher-management.git
    ```

2. Navigate to the project directory:
    ```sh
    cd student-teacher-management
    ```

3. Set up a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Ensure you have Redis installed and running. Start the Redis server if it's not already running:
    ```sh
    redis-server
    ```

6. Run the application:
    ```sh
    python app.py
    ```

7. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. **Home Page**: View lists of students and teachers. Use the search bar to filter data based on name or major. Use the dropdown to filter by role (students, teachers, or both).

2. **Add Data**: Click on "Add Student/Teacher" to add new entries. Fill in the form with the required details and submit.

3. **Reset Database**: Click on the "Reset Database" button to reset the database to its initial state with predefined majors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

If you find this project useful, please consider giving it a star on GitHub. Your feedback and support are greatly appreciated!
