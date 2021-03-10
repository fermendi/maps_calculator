#
# @file <user.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

from common import Functions


class User:
    def __init__(self, current, destination, transport, duration_normal, duration_user, distance):
        self.set_current_place = current
        self.destination_place = destination
        self.transport = transport
        self.duration_normal = duration_normal
        self.duration_user = duration_user
        self.distance = distance

    def run(self):
        Functions.print_result(self.set_current_place,
                               self.destination_place,
                               self.transport,
                               self.duration_user,
                               self.distance,
                               'Your')

        Functions.print_observation(self.duration_normal,
                                    self.duration_user,
                                    self.distance)

#-------------------------------------------------------------------------------------------
#------------------------------------------Main---------------------------------------------
#-------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass