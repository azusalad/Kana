# Kana
Performance based flashcard program.  The program will learn what flashcards you are good at and bad.  The program looks at things like if you got the flashcard correct, time taken to answer, and user input.  Performance is saved when exiting the program.

Currently the code is pretty messy and might not even work.  I have to clean it up.  There is a legacy file `legacy.py` that for sure works.

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
  -m MODE, --mode MODE  Choose flashcard mode or normal mode [flash/normal]
```
Run main.py with the mode you want and the path to your Kana set.  Example: `python main.py -m flash demo.txt` will run flashcard mode on demo.txt.
### Normal mode
In normal mode, you will have to type the value associated with the key shown and the program will check if it is correct.  If your input matches any of the values associated with the key shown, then you will get it correct.  The program will then ask if it was too easy.  If you do not think you need to study that flashcard anymore, type y at the prompt and the program will not show the flashcard for a while.  If your input does not match any of the correct values, then you are given the option to contest the decision.  If you type y, then the program will add your input to the Kana flashcard file as a correct answer.  When you are done playing, type !quit when shown a new flashcard to exit.  Performance will be saved.
### Flashcard Mode
In flashcard mode, you just have to think of the correct answer and the program will ask if you got it right or wrong.  You do not have to type out the value like in normal mode.  When running flashcard mode, the program will first show a key.  Think of the value and then press enter.  The program will then show the correct value(s).  If you got it right just press enter.  If you did not get it right then type `n`.  If you got it right and you think this flashcard is so easy that you do not want to see it again, type `e` for easy.  When you are done playing, type !quit when shown a new flashcard to exit.  Performance will be saved.


## Options
Edit `config.py` to edit performance changes and feedback text.  You can also edit the pictures in `assets/ranks/` with your desired feedback pictures.
