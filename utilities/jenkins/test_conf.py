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

@pytest.mark.parametrize("button_text, xpath", [
    ("Clothing", "//a[contains(text(), 'Clothing')]"),
    ("Accessories", "//a[contains(text(), 'Accessories')]"),
    ("Course", "//a[contains(text(), 'Course')]"),
    ("Stationery", "//a[contains(text(), 'Stationery')]"),
    ("Special-Collection", "//a[contains(text(), 'Special-Collection')]"),
    ("Sale", "//a[contains(text(), 'Sale')]"),
    ("Buy Now!", "//a[contains(text(), 'Buy Now!')]")
])
def test_button_is_enabled(setup, button_text, xpath):
    driver = setup

    try:
        button = driver.find_element("xpath", xpath)
        assert button.is_enabled()
        print(f"{button_text} button is enabled.")
    except Exception as e:
        print(f"Error occurred for {button_text} button: {str(e)}")
        raise

if __name__ == "__main__":
    pytest.main()