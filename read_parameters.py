#
# @file <read_parameters.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import argparse

from common import Functions
from exceptions import ParametersIncompletedException, ParametersFormatException


class ReadParameters:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='maps_calculator information')
        self.parser.add_argument('--current', '-c', dest='current',
                                 type=str, required=False,
                                 help='Current place.')
        self.parser.add_argument('--destination', '-d', dest='destination',
                                 type=str, required=False,
                                 help='Destination place.')
        self.parser.add_argument('--time', '-t', dest='time',
                                 type=str, required=False,
                                 help='Time available (x hr y min) to do the trip.')

        self.args = self.parser.parse_args()

    def get_params(self):
        self.check_params()
        return self.args

    def is_all_params_filled(self):
        return self.args.current is not None and \
               self.args.destination is not None and \
               self.args.time is not None

    def is_all_params_empty(self):
        return self.args.current is None and \
               self.args.destination is None and \
               self.args.time is None

    def define_args(self):
        self.args.current = Functions.get_valid_arg('place', 'Define current place')
        self.args.destination = Functions.get_valid_arg('place', 'Define destination place')
        self.args.time = Functions.get_valid_arg('duration', 'Define your allocated time (ex. 1 hr 10 min, 2.5 hr, 45 min)')

    def check_params(self):
        if self.is_all_params_filled():
            self.args.time = Functions.get_string_to_hours(self.args.time)
            if self.args.time is None:
                raise ParametersFormatException(self.args.time)
        elif self.is_all_params_empty():
            self.define_args()
        else:
            raise ParametersIncompletedException(self.args)


# -------------------------------------------------------------------------------------------
# ------------------------------------------Main---------------------------------------------
# -------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass