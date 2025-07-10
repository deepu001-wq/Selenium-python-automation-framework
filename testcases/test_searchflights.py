import time
import pytest
import softest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.serachflights_results import Search_results_page
from pages.yatra_launchpage import LaunchPage
from utilities.Utils import utils
from ddt import ddt,data,unpack,file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestDemoSearchflights(softest.TestCase):
    log = utils.Custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp=LaunchPage(self.driver)
        self.ut=utils()

    # @data(("New Delhi","New York","1 Stop"),("New Delhi","New York","2 Stops"))
    #@data(*utils.read_data_from_excel("C:/python-selenium/TestFrameworkDemo/testdata/tdataexcel.xlsx", "Flights"))
    @data(*utils.read_data_from_csv("C:/python-selenium/TestFrameworkDemo/testdata/tdata.csv"))
    @unpack
    #@file_data("../testdata/testdata.json")
    def test_demo_search_flights_1Stop(self,goingfrom,goingto,stops):
        #giving from location
        search_flights_results=self.lp.Search_Flights(goingfrom,goingto)
        #to handle dynamic scroll
        self.lp.page_scroll()
        #selecting the filter 1 stop
        search_flights_results.filter_flights_by_stop(stops)
        #verifying that the results show flights having only one stop
        all_stops1=search_flights_results.get_search_flight_results()
        self.log.info(len(all_stops1))
        self.ut.assert_list_items(all_stops1,stops)

    # def test_demo_search_flights_2Stops(self):
    #     search_flights_results=self.lp.Search_Flights("New Delhi","New York")
    #     self.lp.page_scroll()
    #     search_flights_results.filter_flights_by_stop("2 Stop")
    #     all_stops1=search_flights_results.get_search_flight_results()
    #     self.log.info(len(all_stops1))
    #     self.ut.assert_list_items(all_stops1,"2 Stops")













