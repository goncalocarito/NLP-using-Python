import os
from collections import Counter

py_dir = os.path.dirname(os.path.realpath(__file__))

class TextFile(object):
    """Represents a text file with methods to interact with content"""

    def __init__(self, name, path=None):
        self.name = name
        if path is None:
            self.path = "" # searches in the same directory
        else:
            self.path = path
        self.abspath = os.path.join(py_dir, self.path, self.name)
        with open(self.getAbsolutePath(),'r') as content_file:
            content = content_file.read()
        self.content = content

    def getAbsolutePath(self):
        return self.abspath

    def getContent(self):
        return self.content

    # returns a list
    def getWords(self):
        return [word.strip(' .,()":').lower() for word in self.content.split()]

    # returns a list of tuples
    def getWordsOccurence(self):
        # uses Counter from collections library
        return Counter(self.getWords()).most_common()


def printWordsOccurence(words):
    print "\n{0:>20} | {1:>1}".format("Word","Occurrences")
    print " "+ "-"*40
    for (word, count) in words:
        print "{0:>20} | {1:>1}".format(word,count)

def getWordsInCommon(file1, file2):
    return len(set(file1.getWords()).intersection(file2.getWords()))

def printWordsInCommon(file1, file2):
    print "\nThe file {} and {} have {} words in common.\n".format(\
    file1.name, file2.name, getWordsInCommon(file1,file2))

textfile1 = TextFile("50_words_lorem_ipsum_1paragraph.txt", "samplefiles")
textfile2 = TextFile("100_words_lorem_ipsum_1paragraph.txt", "samplefiles")
printWordsOccurence(textfile1.getWordsOccurence())
printWordsInCommon(textfile1, textfile2)
