import random

class Bigram():
    # create instance of bigram with a dictionary of words and dictionary of count of subsequent associations
    def __init__(self):
        self.dict = {}
        self.countdict = {}

    # reads file, please see README.md regarding specific file type
    def read(self, filename):
        content = open(filename, "r", encoding="Latin-1").read().split('\n')
        for line in content:
            arguments = line.split()
            if len(arguments):
                self.add(int(arguments[0]), arguments[1], arguments[2])

    # adds to dictionary: primary word, its subsequent association, and the count of such happening
    def add(self, count, current, subsequent):
        # if already in dictionary, just continue to add to dictionary
        if current in self.dict:
            # check if subsequent association in dictionary
            if subsequent in self.dict[current]:
                self.dict[current][subsequent] += count
            else:
                self.dict[current][subsequent] = count
            self.countdict[current] += count
        # if not in dictionary, create new instance of word
        else:
            self.dict[current] = {}
            self.dict[current][subsequent] = count
            self.countdict[current] = count

    # generates new sentence based on user input parameters
    def generate(self, start, length, threshold):
        newsentence = [start]
        while length > 0:
            nextword = newsentence[len(newsentence) - 1]
            # if nextword isn't included as one in the dictionary, instead of throwing error, 
            # it breaks loop and just prints the sentence, concluding with that word
            if not nextword in self.dict:
                break
            # sums total instances of all occurances of the primary word in question
            total = sum(v for v in list(self.dict[nextword].values()) if float(v)/float(self.countdict[nextword]) > threshold)
            # random generation on distribution to randomly select next word to follow 
            r = int(random.uniform(0, total))
            nsum = 0
            i = 0
            # to find which word is picked next, keep adding all instances until you reach random number—that will be your word
            while nsum < r:
                key = list(self.dict[nextword].keys())[i]
                value = self.dict[nextword][key]
                if float(value)/self.countdict[nextword] > threshold:
                    nsum += value
                i += 1
            newsentence.append(key)
            length -= 1
        return ' '.join(newsentence)

def main():
    # user input
    startword = input('Enter word you want to start with: ')
    slength = int(input('Enter length of generated sentence: '))
    threshold = float(input('Enter threshold of unneeded words, in decimal: '))
    nsentences = int(input('Enter number of sentences generated: '))
    BM = Bigram()
    # i made the sample that's it's drawing from static, but if you input new source, you can substitute w2 file with new file
    BM.read('./w2_.txt')
    # generate new sentences using Bigram model and print
    for i in range(nsentences):
        print(BM.generate(startword, slength, threshold))

if __name__ == '__main__':
    main()