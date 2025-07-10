import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_driver():

    def __init__(self,driver):
        self.driver=driver

    def page_scroll(self):
        # Wait for flight results section to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".content"))
        )

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for content to load

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break  # Scrolling complete
            last_height = new_height

        print("Scrolling complete.")
        time.sleep(2)


    def wait_for_presence_of_all_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements=wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element