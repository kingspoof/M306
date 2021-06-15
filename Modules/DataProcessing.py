#fill the following fields from the dataobject
# 
# specialwords = [[]] With only the special words and their position
# words = [[]] With other words until only the other words

# words and special words have to be arrays of char arrays and they have to be
# the same size


from os import DirEntry
from posixpath import join
from random import randrange


class DataProcessing:

    directions = [1,2,3]
    empty_char = ' '

    def __init__(self):
        print("init dataprocessing")

    def process(self, height, width, general_words, special_words):
        field_words = self.empty_array_with_size(height, width)
        field_words_caps = self.empty_array_with_size(height, width)
        field = self.empty_array_with_size(height, width)

        #place speziel words in array
        field_words = self.place_specific_words(field_words, special_words)
        field_words = self.place_general_words(field_words, general_words)
        for n in field_words:
            print(''.join(n))

        return field_words, field_words_caps, field

    #creates an empty array with the given size
    def empty_array_with_size(self, height, width):
        data = [[self.empty_char] * height for i in range(width)]
        return data

    #puts the special words into the 
    def place_specific_words(self, target, source):
        #print('before')
        #for n in target:
        #    print(''.join(n))

        for word in source:
            try:
                hasspace = True
                x = int(word[0])
                y = int(word[1])
                w = word[2] + ''

                #when the word can be placed, place the word
                direction = randrange(0,4)
                if(self.has_word_space(target, w, x, y, direction)):
                    target = self.place_word_in_space(target, w, x, y, direction)
                else:
                    print(w, 'could not be put in due to size restriction')
            except:
                print(word, ' has invalid coordinates')
        #print('after')
        #for n in target:
        #    print(' '.join(n))
        
        return target

    #place the rest of the words into the field
    def place_general_words(self, target, source):
        for word in source:
            #we will try to place each word 25 times if it does not work by then there is an issue
            for n in range(25):
                x = randrange(0, len(target))
                y = randrange(0, len(target[0]))
                direction = randrange(0,4)
                if(self.has_word_space(target, word, x, y, direction)):
                    self.place_word_in_space(target, word, x, y, direction)
                    break
        return target

    def has_word_space(self, target, word, x, y, direction):
        try:
            if direction == 1:
                for i in range(len(word)):
                    if target[x + i][y + i] != self.empty_char:
                        return False
            elif direction == 2:
                for i in range(len(word)):
                    if target[x + i][y] != self.empty_char:
                        return False
            else:
                for i in range(len(word)):
                    if target[x][y + i] != self.empty_char:
                        return False
        except:
            return False
        return True #if we don't throw an error or quit, we have succeded

    #places the word, does not check if it has space
    def place_word_in_space(self, target, word, x, y, direction):
        if direction == 1: #we try diagonal
            for i in range(len(word)):
                target[x + i][y + i] = word[i].upper()
        elif direction == 2: #then vertical
            for i in range(len(word)):
                target[x + i][y] = word[i].upper()
        else: # if both are not good, we just use horizontal
            word_to_place = word  + ''
            for i in range(len(word_to_place)):
                target[x][y + i] = word_to_place[i].upper()
        return target