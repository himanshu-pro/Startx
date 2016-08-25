import random


class BracketString:
    # initialize the string
    string = ''

    def __init__(self, length):
        for ix in xrange(length):
            # concatenate string with a random bracket
            self.string += random.choice(['[', ']'])

    def checkBalance(self,):
        # maintain state variable representing no. of unbalanced opening brackets
        stack = 0

        for bracket in self.string:
            if bracket == '[':
                stack += 1
            else:
                stack -= 1

            if stack < 0:
                # extra closing bracket
                return False
        
        if stack == 0:
            return True
        else:
            return False

    def getString(self):
        return self.string


for i in xrange(10):
    brackets = BracketString(6)
    print brackets.getString(),' --> ','OK' if brackets.checkBalance() else 'NOT OK'
