#
# @file <maps.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import time

from start_driver import BasePage
from common import Functions, Misc, Locators
from exceptions import RepeatLoopException, NoPossibleTripException
from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException


class Maps(BasePage):
    def __init__(self, driver, current_place_name, destination_place_name):
        super().__init__(driver)
        self.define_cities(current_place_name, destination_place_name)
        self.define_transport(Misc.TRANSPORT)
        self.define_language(Misc.LANGUAGE)
        self.suggestion_place = None
        self.suggestion_place_current = None
        self.suggestion_place_destination = None
        self.duration = 0.1
        self.distance = 0.0

    def load_maps(self):
        print('Load Google Maps ...')
        self.driver.get(Misc.URL_MAPS)
        self.pass_pop_up()

    def pass_pop_up(self):
        time.sleep(Functions.get_time_step())
        try:
            self.driver.switch_to.frame(0)
            self.click(Locators.POPUP_BUTTON)
            self.driver.switch_to.default_content()
        except NoSuchFrameException:
            pass

    def define_cities(self, current_place_name, destination_place_name):
        self.current_place_name = current_place_name
        self.destination_place_name = destination_place_name

    def define_transport(self, transport):
        self.transport = transport

    def define_language(self, language):
        self.language = language

    def send_place(self, locator, place):
        print(f'Defining place: {place} ...')
        self.enter_text(locator, place)

    def set_suggestion(self):
        time.sleep(Functions.get_time_step())
        try:
            elements = self.search_elements(Locators.SUGGESTIONS_PLACES)
            self.suggestion_place = elements[0].text
            elements[0].click()
        except:
            time.sleep(Functions.get_time_step())
            raise RepeatLoopException('Problem to get the suggestions for this place!')

    def get_suggestion(self):
        return self.suggestion_place

    def is_suggestions(self, suggestions):
        return bool(len(suggestions))

    def set_language(self, locator):
        print(f'Defining language: {self.language} ...')
        try:
            self.click(Locators.HAMBURGUER_BUTTON)
            self.click(Locators.LANGUAGE_BUTTON)
            self.click(locator)
            self.driver.refresh()
        except:
            raise RepeatLoopException('Problem to define the language!')

    def set_transport(self, locator):
        print(f'Defining transport: {self.transport} ...')
        self.click(locator)
        time.sleep(Functions.get_time_step())

    def set_navigational(self):
        print('Set navigational function ...')
        self.click(Locators.SEARCH_DIRECTIONS_ICON)

    def get_trip_description(self):
        print(f'Getting the trip description ...')
        try:
            time.sleep(Functions.get_time_step())
            web_element = self.search_element(Locators.TRIP_DESCRIPTION)
            return web_element
        except NoSuchElementException:
            time.sleep(Functions.get_time_step())
            web_element = self.search_element(Locators.NO_POSSIBLE_TRIP)
            print(web_element.text)
            raise NoPossibleTripException

    def get_destination_place(self):
        return self.suggestion_place_destination

    def get_current_place(self):
        return self.suggestion_place_current

    def get_transport(self):
        return self.transport

    def get_duration(self):
        return round(float(self.duration), 2)

    def get_distance(self):
        return round(float(self.distance), 2)

    def run(self):
        self.load_maps()
        self.set_language(Locators.ENGLISH_LANGUAGE)
        self.set_navigational()
        self.set_transport(Locators.TRANSPORT)

        self.send_place(Locators.BOX_CURRENT_PLACE, self.current_place_name)
        self.set_suggestion()
        self.suggestion_place_current = self.get_suggestion()

        self.send_place(Locators.BOX_DESTINATION_PLACE, self.destination_place_name)
        self.set_suggestion()
        self.suggestion_place_destination = self.get_suggestion()

        web_element = self.get_trip_description()

        self.duration = Functions.get_duration_hours(web_element)
        self.distance = Functions.get_distance_km(web_element)

        Functions.print_result(self.suggestion_place_current,
                               self.suggestion_place_destination,
                               self.transport,
                               self.duration,
                               self.distance,
                               'Normal')


#-------------------------------------------------------------------------------------------
#------------------------------------------Main---------------------------------------------
#-------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass