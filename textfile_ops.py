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

    # returns a list or dictionary
    def getWordsOccurence(self):
        # uses set (unsorted list of unique objects) and list method count
        return [(item,self.getWords().count(item)) for item in set(self.getWords())]
        # uses Counter from collections library
        return Counter(self.getWords())


def printWordsOccurence(words):
    pass

textfile1 = TextFile("50_words_lorem_ipsum_1paragraph.txt", "samplefiles")

print textfile1.getAbsolutePath()
print textfile1.getContent()
print textfile1.getWords()
print textfile1.getWordsSET()
print textfile1.getWordsOccurence()
