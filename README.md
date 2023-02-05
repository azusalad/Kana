# Kana
Performance based flashcard program.  The program will learn what flashcards you are good at and bad.  The program looks at things like if you got the flashcard correct, time taken to answer, and user input.

## Usage
### Make a Kana Set
Before you start studying you need to make a Kana flashcard set to study.  Edit maker/terms.txt with the desired key and value pairs you would want to study.  Each flashcard is separated by a blank line.  The first line in
each flashcard is the key.  The following lines are values associated to that key.  For example, let's say you want to put きれい  which means both pretty and clean.  The flashcard in terms.txt would look like this:

```
きれい
pretty
clean
```

After making a terms.txt, run maker.py with `python maker.py`.  The output will be dictionary.txt which is your Kana set.  Rename the set and move the set to where you want.
### Run Main Program
```
usage: main.py [-h] -m MODE input

positional arguments:
  input                 Kana file to study

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Choose flashcard mode or normal mode [f/n]
```
Run main.py with the mode you want and the path to your Kana set.  Example: `python main.py -h f demo.txt`. There are two modes: flashcard mode and normal mode.  In normal mode, you will have to type the value associated with the key shown and the program will check if it is correct.  In flashcard mode, you just have to think of the correct answer and the program will ask if you got it right or wrong.
### Options While Running Main Program

