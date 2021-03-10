#
# @file <maps_calculator.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import sys

from common import Functions
from exceptions import NoPossibleTripException, RepeatLoopException, \
    ParametersIncompletedException, ParametersFormatException, BrowserImplementationException
from read_parameters import ReadParameters
from start_driver import StartDriver, Browser
from maps import Maps
from user import User
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException

#-------------------------------------------------------------------------------------------
#------------------------------------------Main---------------------------------------------
#-------------------------------------------------------------------------------------------

if __name__ == '__main__':
    Functions.credits()
    try:
        parser = ReadParameters()
        args = parser.get_params()

        start_driver = StartDriver(Browser.CHROME)

        b_repeat = True
        while b_repeat:
            try:
                maps = Maps(start_driver.driver,
                            args.current,
                            args.destination)

                maps.run()

                user = User(maps.get_current_place(),
                            maps.get_destination_place(),
                            maps.get_transport(),
                            maps.get_duration(),
                            Functions.get_string_to_hours(args.time),
                            maps.get_distance())

                user.run()

            except RepeatLoopException as ex:
                print(f'{ex}, Increase delay and reloading ...')
                Functions.increase_time_step(2)
            else:
                print(f'End program successfully!')
                b_repeat = False

    except KeyboardInterrupt:
        print(f'\nCTRL+C!')
    except TimeoutException as ex:
        print(f'TimeoutException: {ex}')
    except NoSuchElementException as ex:
        print(f'NoSuchElementException: {ex}')
    except WebDriverException as ex:
        print(f'WebDriverException: {ex}')
    except NoPossibleTripException as ex:
        print(f'Unable to find a route (maybe try a boat or a plane)!')
    except ParametersIncompletedException as ex:
        print(f'ExceptionParametersIncompleted: {ex}')
        print('Please complete all the parameters or run without any of them!')
    except ParametersFormatException as ex:
        print(f'ExceptionParametersFormat: {ex}')
    except BrowserImplementationException as ex:
        print(f'ExceptionBrowserImplementation: {ex}')
    finally:
        print(f'Exit program!')
        sys.exit()