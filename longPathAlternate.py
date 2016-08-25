import csv


def maxIndices(mList):
    res = []
    if mList:
        # assume the first to be max
        maxVal = mList[0]

        for k, val in enumerate(mList):
            if val == maxVal:
                # plausible candidate for max
                res.append(k)

            elif val > maxVal:
                # new max level
                maxVal = val
                res = [k]
    return res


class WordsGame:

    # User defined word list
    wordList = []
    # Length of word list
    listLen = None

    # Graph with word indices as vertices and an edge represented by a 1
    # Edge from word-a to word-b exists if the last char of word-a matches the first of word-b
    graph = None

    def __init__(self, filePath):
        with open(filePath, 'r') as fileDp:
            self.wordList = list(csv.reader(fileDp))[0]
        self.listLen = len(self.wordList)

        # initialize the graph with no edges and appropriate no. of vertices
        self.graph = [[0 for i in xrange(self.listLen)] for j in xrange(self.listLen)]

        self.populateGraph()

    def populateGraph(self):
        for wordx in xrange(self.listLen):
            for wordy in xrange(self.listLen):
                if wordx != wordy and self.wordList[wordx][-1] == self.wordList[wordy][0]:
                    # create edge from wordx to wordy
                    self.graph[wordx][wordy] = 1
                wordy += 1
            wordx += 1

    def solve(self):
        result = []
        # check paths starting with each word
        for i in xrange(self.listLen):
            # initial path is just the word itself
            result.extend(self.getPaths([i]))
        # get the word sequences for each of the longest path in result
        return [[self.wordList[x] for x in result[index]] for index in maxIndices([len(v) for v in result])]

    def getPaths(self, path):
        # Explore new paths
        possibilities = [path + [j] for j in xrange(self.listLen) if self.graph[path[-1]][j] == 1 and j not in path]

        if possibilities:
            result = []
            for newPath in possibilities:
                result.extend(self.getPaths(newPath))
            return result
        else:
            return [path]

with open('bazinga.txt', 'w') as fileDp:
    for x in WordsGame(raw_input('Enter file path: ')).solve():
        fileDp.writelines(' --> '.join(x) + '\n')
