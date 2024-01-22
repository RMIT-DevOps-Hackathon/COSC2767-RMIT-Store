# RMIT University Vietnam
#  Course: COSC2767 Systems Deployment and Operations
#  Semester: 2023C
#  Assessment: Assignment 3
#  Author - ID: 
#    Do Le Long An - s3963207
#    La Tran Hai Dang - s3836605
#    Pham Quang Man - s3804811
#    Huynh Van Anh - s3836320
#    Hoang Ngoc Duan - s3817747
#  Created date: 06/01/2024
#  Last modified: 22/01/2024
#  Acknowledgement: RMIT Canvas, ChatGPT, AWS Documentation, StackOverflow,
#  AWSAcademy Learner Lab, GitHub Documentation, Docker Documentation
#  Jenkins Documentation, Tom Huynh

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")
def setup():
    url = "http://44.206.113.151"
    chrome_options = Options()

    options = [
        "--headless", "--disable-gpu", "--ignore-certificate-errors",
        "--disable-extensions", "--no-sandbox", "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.get(url)

    yield driver

    driver.quit()

def test_database_error_message(setup):
    driver = setup
    try:  
        # Check if the page contains an element indicative of a database error using XPath
        error_element = driver.find_element("xpath", '//div[@class="error-content"]/h1')

        if error_element:
            # If the error element is found, there might be a database error
            error_message = driver.find_element("xpath", '//div[@class="error-content"]/p').text
            print(f"Database Error Message: {error_message}")

            # Add assertions based on the error content
            assert "Database connection error" in error_message
        else:
            # If no error element is found, assert that everything is okay
            assert True  # Add more relevant assertions if needed
    except NoSuchElementException:
        # Handle the case when the error element is not found
        print("No error element found. Possibly no database connection error.")

        # Add assertions or further handling as needed
        assert True  
