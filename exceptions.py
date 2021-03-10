#
# @file <exceptions.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

class BrowserImplementationException(Exception):
    def __init__(self, browser_name, message="Please implement this browser!"):
        self.browser_name = browser_name
        self.message = message
        super().__init__(f'\n{message}')

    def __str__(self):
        return f'\n{self.message}\nBrowser: {self.browser_name}'


class NoPossibleTripException(Exception):
    def __init__(self, message="Unable to find a route!"):
        super().__init__(f'\n{message}')


class RepeatLoopException(Exception):
    def __init__(self, description, message="Error getting the information from Google maps!"):
        self.message = message
        self.description = description
        super().__init__(f'\n{message}')

    def __str__(self):
        return f'\n{self.message}:' \
               f'\n{self.description}'


class ParametersIncompletedException(Exception):
    def __init__(self, args, message="Parameters are not completed!"):
        self.arguments = args
        self.message = message
        super().__init__(f'\n{self.message}')

    def __str__(self):
        return f'\n{self.message} -> ' \
               f'\nCurrent place: {self.arguments.current}' \
               f'\nDestination place: {self.arguments.destination} ' \
               f'\nAllocate time: {self.arguments.time}'


class ParametersFormatException(Exception):
    def __init__(self, message="Parameters time (duration) with a format error!"):
        super().__init__(f'\n{message}')


#-------------------------------------------------------------------------------------------
#------------------------------------------Main---------------------------------------------
#-------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass