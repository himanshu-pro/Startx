import re


class Splitter:
    badpattern = re.compile("\.((?= [a-z])|(?=[0-9.,;]))|((?<=((.|\n)Mr)|(Mrs)|((.|\n)Dr))\.(?= [A-Z]))|(?<=[a-zA-Z])\.(?=[a-zA-Z])")
    netPattern = re.compile("[.?!]")
    text = None
    filePath = None

    def __init__(self, filePath):
        self.filePath = filePath
        with open(filePath, 'r') as fileDp:
            self.text = fileDp.read()

    def getBounds(self):
        string = ' ' + self.text  # solves a limitation of the regex used to recognize titles in the beginning of text

        # all the possible sentence boundaries
        netPeriods = set([m.start() for m in self.netPattern.finditer(string)])

        # sentence boundaries excluded by the required conditions
        badPeriods = set([m.start() for m in self.badpattern.finditer(string)])

        # legitimate sentence boundaries
        splitx = sorted(list(netPeriods - badPeriods))

        # balance the initial offset
        splitx = [i-1 for i in splitx]

        return splitx

    def splitFile(self):
        start = 0
        result = []
        for i in self.getBounds():
            result.append(self.text[start:i+1]+"\n")
            start = i+1
        print result
        with open(self.filePath,'w') as fileDp:
            fileDp.writelines(result)


splitter = Splitter(raw_input('Enter file path: '))
splitter.splitFile()
