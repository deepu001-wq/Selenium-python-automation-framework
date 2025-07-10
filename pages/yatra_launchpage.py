import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.Base_driver import Base_driver
from pages.serachflights_results import Search_results_page
from utilities.Utils import utils


class LaunchPage(Base_driver):
    log = utils.Custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        #self.wait = wait


    #locators
    depart_locator="//p[@title='New Delhi']"
    input_field="//input[@id='input-with-icon-adornment']"
    first_suggestion="//li[contains(@class,'css-1546kn3')]"

    going_to_field = "//p[normalize-space()='BOM, Chhatrapati Shivaji International']"
    going_to_input = "//input[@id='input-with-icon-adornment']"
    going_to_results = "//div[@class='MuiBox-root css-134xwrj']//div[@class='MuiBox-root css-0']/li//div[@class='fw-600 mb-0']"

    date_field = "//div[@class='css-w7k25o']"
    all_dates_field = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[@class='react-datepicker__week']/div"
    search = "//button[normalize-space()='Search']"


    def enterDepartfromlocation(self,departlocation):
        self.wait_until_element_is_clickable(By.XPATH,self.depart_locator).click()
        self.wait_until_element_is_clickable(By.XPATH, self.input_field).send_keys(departlocation)
        self.wait_until_element_is_clickable(By.XPATH, self.first_suggestion).click()

    def enterGoingtolocation(self,goingtolocation):

        self.wait_until_element_is_clickable(By.XPATH,self.going_to_field).click()
        time.sleep(2)
        self.wait_until_element_is_clickable(By.XPATH,self.going_to_input).send_keys(goingtolocation)
        time.sleep(2)
        search_results = self.wait_for_presence_of_all_elements(By.XPATH,self.going_to_results)
        for results in search_results:
            self.log.info(results.text)
            if "New York, (JFK)" in results.text:
                results.click()
                time.sleep(2)
                break

    def enterdate(self):

        self.wait_until_element_is_clickable(By.XPATH,self.date_field).click()
        all_dates=self.driver.find_elements(By.XPATH,self.all_dates_field)
        for dates in all_dates:
            if "29" in dates.text:
                dates.click()
                break

    def clicksearch(self):
        self.driver.find_element(By.XPATH,self.search).click()
        time.sleep(5)

    def Search_Flights(self,departlocation,goingtolocation):
        self.enterDepartfromlocation(departlocation)
        self.enterGoingtolocation(goingtolocation)
        self.enterdate()
        self.clicksearch()
        search_flights_results=Search_results_page(self.driver)
        return search_flights_results


# def Departfrom(self, departlocation):
    #
    #     #depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='DEL, Indira Gandhi International']")))
    #     depart_from=self.wait_until_element_is_clickable(By.XPATH, "//p[normalize-space()='DEL, Indira Gandhi International']")
    #     depart_from.click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//input[@id='input-with-icon-adornment']").send_keys(departlocation)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//li[contains(@class,'css-1546kn3')]").click()



 # def goingto(self,goingtolocation):
    #
    #     #going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='BOM, Chhatrapati Shivaji International']")))
    #     going_to=self.wait_until_element_is_clickable(By.XPATH, "//p[normalize-space()='BOM, Chhatrapati Shivaji International']")
    #     going_to.click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//input[@id='input-with-icon-adornment']").send_keys(goingtolocation)
    #     time.sleep(2)
    #     # search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
    #     # # "//div[@class='MuiBox-root css-134xwrj']//div[@class='MuiBox-root css-0']/li//div[@class='fw-600 mb-0']")))
    #     search_results = self.wait_for_presence_of_all_elements(By.XPATH,
    #     "//div[@class='MuiBox-root css-134xwrj']//div[@class='MuiBox-root css-0']/li//div[@class='fw-600 mb-0']")
    #
    #     for results in search_results:
    #         print(results.text)
    #         if "New York, (JFK)" in results.text:
    #             results.click()
    #             time.sleep(2)
    #             break


  # def date(self):
    #     #self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-w7k25o']"))).click()
    #     self.wait_until_element_is_clickable(By.XPATH, "//div[@class='css-w7k25o']").click()
    #     all_dates = self.driver.find_elements(By.XPATH,
    #                                           "//body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[@class='react-datepicker__week']/div")
    #
    #     for dates in all_dates:
    #         if "29" in dates.text:
    #             dates.click()
    #
    #             break