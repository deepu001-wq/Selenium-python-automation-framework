import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.Base_driver import Base_driver
from utilities.Utils import utils


class Search_results_page(Base_driver):
    log=utils.Custom_logger(loglevel=logging.WARNING)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        #self.wait=wait

    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stops')]"

    def get_filter_by_one_stop_icon(self):
            return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
            return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_2_STOP_ICON)


    def get_filter_by_non_stop_icon(self):
            return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)


    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("Selected flights with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stops":
            time.sleep(5)
            self.get_filter_by_two_stop_icon().click()
            self.log.warning("Selected flights with 2 stops")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            self.log.warning("Selected non stop flights")
            time.sleep(2)
        else:
            print("Please provide valid filter option")


