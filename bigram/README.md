# Bigram model

Creation of a Bigram model. Uses Bigram model to randomly generate sentences, based on other writing

## What is a Bigram model — Theoretical

A bigram is a sequence of 2 items, taken from a string of tokens. The bigram model calculates instances occuring bigrams to find a the probability of one token following a primary token. For example, take the following string of tokens:

"The quick brown fox jumps over the lazy dog"

If we break this down into bigram probabilities, we get:

```
the: {quick: 1, lazy: 1}
quick: {brown: 1}
brown: {fox: 1}
fox: {jumps: 1}
over: {the: 1}
lazy: {dog: 1}
```

Well, not quite probabilities, but these are the bigram instances. So, in this case, the probability for the token 'fox' following the token 'brown' is 100%. Meanwhile, the probility of the token 'quick' following the token 'the' is only 1 out of 2, or 50%.

As you can imagine, as we increase the number of tokens (tokens don't have to be words btw. They can be characters or symbols. Depends on the project), probabilities will shift a lot more. And given a large enough body of tokens, you'll get a much better idea of what tokens will follow other tokens. This will be performed via random selection based on the bigram probability distribution that we establish based on previous text, much like we have above. 

Threshold: So, given these probabilities, we might inevitably have some irrelevant outliers occur that we want to parse out. For example, let's say we're trying to tokenize a research paper about Christian religious text. Phrases like "Holy Spirit" or "Holy Father" or others would be plentiful. Now, let's see that there's one silly reference to someone who says the phrase "Holy moley". Now, that's only once out of, let's say 1000 references of the word "holy". Even so, that means there's a 1 in 1000 chance that when generating a new sentence, the word "holy" will be followed by the word "moley", which is merely an outlier that we don't want to keep. So, we set our threshold to 0.001, or 1/1000. In other words, the succeeding word needs to have greater than a 1 in 1000 chance of happening for it to be included in the probability calculation. Therefore, we eliminate the probability of our program generating any sentence with the phrase "holy moley".

## This project

In this project, I use words as tokens and I try to generate new sentences based on these probabililty distributions. However, I did not tokenize a passage. That's certainly doable—but I simply used a pre-tokenized passage for ease of use. You can see this in the 'w2_.txt' file.

## Files in bundle

- bigram.py: Main program. Please see this file for the code.

- w2_.txt: The "database" if you will. (not included. read on...)

## Installation

Need Python 3 installed

go to http://www.ngrams.info/download_coca.asp and download the non case sensitive 2-grams. Save this in the same folder as the bigram.py file and name it *w2_.txt*

## Step by Step

1) Run bigram.py in terminal:

```
Terminal: python bigram.py
```

2) The program will prompt the user for parameters:

```
Enter word you want to start with: *generic english words should do. if program ends without doing anything, word might be too esoteric*
Enter length of generated sentence: *don't make it too long. 10 is probably max if you don't want to wait too long*
Enter threshold of unneeded words, in decimal: *see bigram model - theoretical. i usually use 0.01*
Enter number of sentences generated: *however many you want. or you can run the program again and again. Try <10 to avoid long runtime*
```

My sample
```
Enter word you want to start with: there
Enter length of generated sentence: 5
Enter threshold of unneeded words, in decimal: 0.01
Enter number of sentences generated: 5
```

If it takes too long Control-C (on Mac) should terminate process. Input smaller parameters to resolve

3) Wait for results :)