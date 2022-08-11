import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


def selenium_easy():

    # for windows add driver path like this
    os.environ['PATH'] += r"F:/SeleniumWebdrivers"
    driver = webdriver.Chrome()

    driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
    # waiting for 3 seconds if the element is already there it will not wait for 3 seconds
    # it will git initbe applied across all the elements
    driver.implicitly_wait(3)

    download_btn = driver.find_element(By.ID, value='downloadButton')
    download_btn.click()

    try:
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element(
                # Element Filtration
                (By.CLASS_NAME, 'progress-label'),
                'Complete!'  # The Expected Text
            )
        )
    except Exception as e:
        print(str(e) + "Could not find text")


if __name__ == "__main__":
    selenium_easy()
