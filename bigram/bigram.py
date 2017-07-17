import random

class Bigram():
    def __init__(self):
        self.dict = {}
        self.countdict = {}

    def read(self, filename):
        content = open(filename, "r", encoding="Latin-1").read().split('\n')
        for line in content:
            arguments = line.split()
            if len(arguments):
                self.add(int(arguments[0]), arguments[1], arguments[2])

    def add(self, count, current, precedent):
        if current in self.dict:
            if precedent in self.dict[current]:
                self.dict[current][precedent] += count
            else:
                self.dict[current][precedent] = count
            self.countdict[current] += count
        else:
            self.dict[current] = {}
            self.dict[current][precedent] = count
            self.countdict[current] = count

    def generate(self, start, length, threshold):
        newsentence = [start]
        while length > 0:
            nextword = newsentence[len(newsentence) - 1]
            # if nextword isn't included as one in the dictionary, instead of throwing error, 
            # it breaks loop and just prints the sentence, concluding with that word
            if not nextword in self.dict:
                break
            total = sum(v for v in list(self.dict[nextword].values()) if float(v)/float(self.countdict[nextword]) > threshold)
            r = int(random.uniform(0, total))
            nsum = 0
            i = 0
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
    startword = input('Enter word you want to start with: ')
    slength = int(input('Enter length of generated sentence: '))
    threshold = float(input('Enter threshold of unneeded words, in decimal: '))
    nsentences = int(input('Enter number of sentences generated: '))
    # startword = 'fixer'
    # slength = 5
    # threshold = 0.0000001
    # nsentences = 1
    BM = Bigram()
    BM.read('/Users/JustinZhou/Documents/Programming/College CS classes/class projects/bigram/w2_.txt')
    sentences = []
    for i in range(nsentences):
        # sentences.append(BM.generate(startword, slength, threshold))
        print(BM.generate(startword, slength, threshold))
    # for sentence in sentences:
    #     print(sentence)

if __name__ == '__main__':
    main()