#
# @file <common.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import os
import random

from selenium.webdriver.common.by import By

global_var_delay = 3


class Path:
    PATH = os.path.expanduser('~') + '/maps_calculator/'
    CHROMEDRIVER_FILE = 'chromedriver/chromedriver'


class Unit:
    HOUR_UNIT = 'hr'
    MINUTS_UNIT = 'min'
    KILOMETER_UNIT = 'km'
    SPEED_UNIT = 'km/h'
    METER_UNIT = 'm'
    SECOND_UNIT = 's'


class Misc:
    SEPARATOR = "-" * 70
    URL_MAPS = 'https://www.google.com/maps/'
    LANGUAGE = 'English'
    TRANSPORT = 'Car'
    DELTA_SPEED = 0.5
    LONG_TRIP_HR = 8


class Speed:
    VERY_SLOW = range(0, 20)
    SLOW = range(20, 40)
    MEDIUM = range(40, 80)
    FAST = range(80, 150)
    VERY_FAST = range(150, 400)


class Transport:
    REVERSE = ['turtle', 'tricycle']
    VERY_SLOW = ['walk', 'horse', 'bicycle', 'skate', 'rollers']
    SLOW = ['motorbike', 'electric bike']
    MEDIUM = ['Honda e', 'Fiat 500', 'Dodge Caravan']
    FAST = ['Toyota Camry', 'Audi TT', 'Renault Sandero']
    VERY_FAST = ['Bugatti Veyron', 'Ford GT90', 'Tesla Roadster', 'Audi R8']
    NON_SENSE = ['rocket', 'missile']


class Locators:
    POPUP_BUTTON = (By.XPATH, '//*[@id="introAgreeButton"]/span/span')
    BOX_CURRENT_PLACE = (By.XPATH, '//*[@id="sb_ifc51"]/input')
    BOX_DESTINATION_PLACE = (By.XPATH, '//*[@id="sb_ifc52"]/input')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="searchbox-searchbutton"]')
    SEARCH_DIRECTIONS_ICON = (By.ID, 'searchbox-directions')
    SUGGESTIONS_PLACES = (By.CLASS_NAME, 'sbsb_c')
    TRIP_DESCRIPTION = (By.XPATH, '//*[@id="section-directions-trip-0"]/div/div[1]')
    NO_POSSIBLE_TRIP = (By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[6]/div/jsl')
    HAMBURGUER_BUTTON = (By.XPATH, '//*[@id="omnibox-singlebox"]/div[1]/div[1]/button')
    LANGUAGE_BUTTON = (By.XPATH, '//*[@id="settings"]/div/div[2]/ul/ul[2]/li[2]/button')

    TRANSPORT = (By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button/img')
    ENGLISH_LANGUAGE = (By.XPATH, '//*[@id="languages"]/div/div[2]/div[2]/ul[1]/li[11]/a')


class Functions:
    @staticmethod
    def credits():
        print(Misc.SEPARATOR)
        print('maps_calculator: Bot to calculate normal and custom trip conditions.')
        print('Fernando Mendiburu - 2021')
        print(Misc.SEPARATOR)

    @staticmethod
    def get_option(web_elements):
        option = None
        b_correct_option = False
        container_w_e = web_elements
        while not b_correct_option:
            print('\nOptions:')
            for i, web_element in enumerate(container_w_e, 1):
                text = web_element.text.split("\n")[0]
                print(f'{i}. {text}')
            option = input('\nChoose the option: ')
            b_correct_option = Functions.verify(option, container_w_e)
        return int(option)

    @staticmethod
    def verify(option, elements):
        try:
            if 0 < int(option) <= len(elements):
                return True
            else:
                print('Invalid option!')
                return False
        except:
            print('Invalid option!')
            return False

    @staticmethod
    def get_string_to_hours(string):
        list_duration = string.split(' ')
        if len(list_duration) == 4 and list_duration[1] == Unit.HOUR_UNIT and \
                list_duration[3] == Unit.MINUTS_UNIT:
            return round(float(list_duration[0]) + float(list_duration[2])/60, 2)
        elif len(list_duration) == 2 and list_duration[1] == Unit.MINUTS_UNIT:
            return round(float(list_duration[0])/60, 2)
        elif len(list_duration) == 2 and list_duration[1] == Unit.HOUR_UNIT:
            return round(float(list_duration[0]), 2)
        print('Problem to get the duration format!')
        return None

    @staticmethod
    def get_string_to_kilometers(string):
        if string.find(Unit.KILOMETER_UNIT):
            dist_str = string.split(' ')[0]
            dist_str = dist_str.replace(',', '')
            return round(float(dist_str), 2)
        else:
            print('Problem to get the distance format!')

    @staticmethod
    def get_duration_hours(web_element):
        try:
            return Functions.get_string_to_hours(web_element.text.split("\n")[0])
        except:
            print('Problem to get the duration of this trip!')

    @staticmethod
    def get_distance_km(web_element):
        try:
            return Functions.get_string_to_kilometers(web_element.text.split("\n")[1])
        except:
            print('Problem to get the distance of this trip!')

    @staticmethod
    def increase_time_step(delta_t):
        global global_var_delay
        global_var_delay += delta_t
        print(f'Set new time step: {global_var_delay}{Unit.SECOND_UNIT}!')

    @staticmethod
    def get_time_step():
        global global_var_delay
        return global_var_delay

    @staticmethod
    def is_not_valid_arg(arg):
        if arg is None or arg is '' or arg == 0:
            print('Invalid value. Insert the correct one!')
            return True
        else:
            return False

    @staticmethod
    def get_valid_arg(type, prompt):
        is_invalid_arg = True
        arg = None
        while is_invalid_arg:
            try:
                if type == 'place':
                    arg = str(input(f'{prompt}: '))
                if type == 'duration':
                    arg = Functions.get_string_to_hours(input(f'{prompt}: '))
                is_invalid_arg = Functions.is_not_valid_arg(arg)
            except ValueError:
                pass
        return arg

    @staticmethod
    def get_mean_speed(distance, duration):
        return round(distance/duration, 2)

    @staticmethod
    def is_faster_than_normal(speed, reference):
        reference_augmented = reference + reference * Misc.DELTA_SPEED
        return speed > reference_augmented

    @staticmethod
    def is_slower_than_normal(speed, reference):
        reference_augmented = reference - reference * Misc.DELTA_SPEED
        return speed < reference_augmented

    @staticmethod
    def get_mean_transport(speed):
        speed = int(speed)
        if speed < 0:
            return random.choice(Transport().REVERSE)
        elif speed in Speed.VERY_SLOW:
            return random.choice(Transport().VERY_SLOW)
        elif speed in Speed.SLOW:
            return random.choice(Transport().SLOW)
        elif speed in Speed.MEDIUM:
            return random.choice(Transport().MEDIUM)
        elif speed in Speed.FAST:
            return random.choice(Transport().FAST)
        elif speed in Speed.VERY_FAST:
            return random.choice(Transport().VERY_FAST)
        else:
            return random.choice(Transport().NON_SENSE)

    @staticmethod
    def is_long_trip(time):
        return time >= Misc.LONG_TRIP_HR

    @staticmethod
    def print_duration_beauty(duration):
        if duration < 1:
            return f'{int(duration * 60)} {Unit.MINUTS_UNIT}'
        else:
            return f'{round(duration, 2)} {Unit.HOUR_UNIT}'

    @staticmethod
    def print_distance_beauty(distance):
        if distance < 1:
            return f'{int(distance * 1000)} {Unit.METER_UNIT}'
        else:
            return f'{round(distance, 2)} {Unit.KILOMETER_UNIT}'

    @staticmethod
    def print_fast_slow(speed, reference):
        if Functions.is_faster_than_normal(speed, reference):
            print('You should go faster (dangerously?) than normal trip.')
            print(f'A suggested transport could be: {Functions.get_mean_transport(speed)}!')
        elif Functions.is_slower_than_normal(speed, reference):
            print('You can go slower than normal trip!')
        else:
            print('Enjoy the trip and be careful!')

    @staticmethod
    def print_is_long_trip(time, conditions):
        if Functions.is_long_trip(time):
            print(f'{conditions} conditions: Stops are not considered. It will take you more time!')
        else:
            pass

    @staticmethod
    def print_result(place_current,
                     place_destination,
                     transport,
                     duration,
                     distance,
                     conditions):
        mean_speed = Functions.get_mean_speed(distance, duration)

        print(f'\n{Misc.SEPARATOR}')
        print(f'{conditions} conditions:')
        print(f'{place_current} -> {place_destination}')
        print(f'Transport: {transport}')
        print(f'{conditions} duration: {Functions.print_duration_beauty(duration)}. '
              f'Distance: {distance} {Unit.KILOMETER_UNIT}')
        Functions.print_is_long_trip(duration, conditions)
        print(f'Mean speed: {mean_speed} {Unit.SPEED_UNIT}.')
        print(Misc.SEPARATOR)

    @staticmethod
    def print_observation(duration_maps,
                          duration_user,
                          distance):

        mean_speed_maps = Functions.get_mean_speed(distance, duration_maps)
        mean_speed_user = Functions.get_mean_speed(distance, duration_user)
        print(f'\n{Misc.SEPARATOR}')
        print(f'Observations:')
        Functions.print_fast_slow(mean_speed_user, mean_speed_maps)

        print(Misc.SEPARATOR)


#-------------------------------------------------------------------------------------------
#------------------------------------------Main---------------------------------------------
#-------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass