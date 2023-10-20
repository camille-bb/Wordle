''' 
Wordle Solver Class Version

Creator: Camille Beck-Belaman
Date: 2022
'''



import Wordle_Solver
import random

print("Get started by creating an instance x of Word with --> x = Wordle_Class.Word()")

class Word():
    '''This Class records the elements of the guess to then give out all the possible words

    _alphabet--> Mutable List of all the string Letters not in the guess
    _oranges--> Mutable list of all the words 
    _green--> guess of letters in word with _ representing empty and all letters being green
    _location --> list of lists of letters that don't belong in that location
    '''

    def GetAlphabet(self):
        return self._alphabet

    def SetAlphabet(self, alphabet):
        assert(type(alphabet)==list)
        self._alphabet = alphabet

    def GetOranges(self):
        return self._oranges

    def SetOranges(self, oranges):
        assert(type(alphabet)==list)
        self._oranges = oranges
    
    def GetGreen(self):
        return self._guess

    def SetGreen(self, green):
        assert(type(green)==str)
        assert(len(green)==5)
        self._green = green

    def GetLocation(self):
        return self._location

    def SetLocation(self, location):
        assert(type(location)==list)
        assert(len(location)==5)
        self._location = location


    def __init__(self):
        '''initialise the alphabet (aka list of non_letters), oranges, and position of known letters'''
        self._alphabet = []
        self._oranges = []
        self._green = '_____'
        self._location = [[],[],[],[],[]]
        self._library = Wordle_Solver.library
        print("")
        print(self.play())


    def play(self):
        '''Method called in initialiser to actually play everything smoothly'''
        print("Welcome to the interactive Wordle Solver (Class Edition)! ")
        counter = 6
        state = "PLAY"
        while len(self._library) > 1 and state == "PLAY":
            print("")
            print( "You have " + str(counter ) + " chances left.")
            print("")
            print("Choose a Word and input it.")
            print(self.random())
            print("")
            keep = input("Was the Guess Correct? (YES or NO)  ")
            if keep == "YES":
                state = "WIN"
            else:
                if counter == 0:
                    keep = input("You have no more chances. Keep Playing? (YES or NO)  ")
                    if keep == "NO":
                        state = "LOST"
                    else:
                        counter = "no"
                        self.update_all()
                elif counter == "no":
                    keep = input("Keep Playing? (YES or NO)  ")
                    if keep == "NO":
                        state = "LOST"
                else:
                    counter -= 1
                    self.update_all()   
        if state == "WIN" or len(self._library) == 1:
            print("")
            return "Game Over. You Won with " + str(counter-1) + " chances left!"
        elif state == "LOST":
            return "Game Over. You Lost."
        

    def update_all(self):
        '''updates the alphabet, oranges and guess based'''
        print("")
        self.update_alphabet()
        print("")
        self.update_green()
        print("")
        self.update_orange()
        print("")
        self.update_location()
        print("")
        self.remove_double_words()
        print(self.options())

        
    def update_alphabet(self):
        '''interactive list of all the non-letters'''
        amount = int(input('How many new grey letters are there? (Ignore Repeats) --> '))
        for i in range(amount):
            letter = input('letter --> ')
            assert len(letter) == 1, 'the letter is not the right length'
            self._alphabet.append(letter)


    def update_green(self):
        '''updates guess'''
        new_green = input("What is the new guess (_____ format)?  ")
        self.SetGreen(new_green)


    def update_orange(self):
        '''updates oranges by asking for new ones'''
        amount = int(input("How many new orange letters are there?  "))
        for i in range(amount):
            orange = input("orange letter -->  ")
            self._oranges.append(orange)


    def update_location(self):
        "updates location based on the position of the letters"
        amount = int(input("How many new orange letters are in new positions?  "))
        for i in range(amount):
            position = int(input("position -->  "))
            letter = input("letter -->  ")
            self._location[position -1].append(letter)
        

    def options(self):
        '''Returns the options for words that could be possibilities under the form of a list or str and a message of total options'''
        '''puts together all the prior helper functions to actually sort through the list and offer answers
        library is list of all the possible words that we will sort through; list of strings with each len(4)
        '''
        #first_list is a list with all the words that don't include the forbidden letters
        first_list = Wordle_Solver.fuckinhell(self._library, self._alphabet)
       
        #sec_list sorts out all the words of the list that don't work with the guess
        sec_list= Wordle_Solver.sort2(first_list, self._green)
    
        #third_list removes all the words that don't include the orange letters
        third_list = Wordle_Solver.orange4(sec_list,self._oranges)

        #final_list removes all the words that have orange letters in the wrong place
        final_list = Wordle_Solver.sort_location(third_list, self._location)

        self._library = final_list
        self.remove_double_words()

        assert self._library != [], "No available words fit the criteria."
        if len(self._library)==1:
            return str("The Answer is " + str(self._library[0]) + "!!!")
        else:
            return self._library, (str(len(self._library))+ " possible answers")


    def remove_double_words(self):
        '''sorts out all repeat words in a list'''
        for word in self._library:
            amount = self._library.count(word)
            while amount > 1:
                self._library.remove(word)
                amount = amount = self._library.count(word)
            
   
    def random(self):
        '''returns a random word from the available words'''
        better_list = self.sort_doubles(self._library)
        #if len(better_list) != 0:
        #    x = random.randint(1,len(better_list))
         #   return "Word Suggestion (premium): " + str(better_list[x-1])
        #else:
        x = random.randint(1,len(self._library))
        return "Word Suggestion: " + str(self._library[x-1])


    def sort_doubles(self, list):
        '''returns a list whithout any words that include double or more letters'''
        new_list = list.copy()
        for word in new_list:
            counter = 0
            for letter in word:
                for i in range(5):
                    if word[i] == letter:
                        counter += 1
            if counter > 5:
                new_list.remove(word)
        return new_list

#- cd Wordle
#- python
#- import Wordle_Class

#Things to do: sort out letters that are green but false repeat; give most likely random based on no repeats;skip some steps if obvious like if 5 grey
#Bugs: make faster; premium is wrong sometimes
