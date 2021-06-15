# fill the following field from the datamodel
# height = the height of the field
# widht = the width of the field
# all_words = a array of all possible words as array
# spezial_words = spezial words in the following format [x, y, word]

import os.path

class DataInput:
    def __init__(self):
        print('init DataInput')


    #get data from user, returns height, width, general_word_list, spezial_word_list
    def process(self):
        #gets the height
        #########height = self.get_number_input('Height: ')
        height = 200
        #gets the width
        #########width = self.get_number_input('Width: ')
        width = 200
        #gets the general words
        #########word_list_file = self.get_input_file('Input file to general word list: ')
        word_list_file = '/Users/lucienkaser/Desktop/general.txt'
        general_word_list = self.file_to_list(word_list_file)
        general_word_list = self.remove_double_words(general_word_list)
        self.print_all_lines_in_list(general_word_list, 'Your words: ')

        #gets the spezial words
        spezial_word_list = []
        #######if(self.yes_no_Question('Do you want to input spezial words?','y','n')):
        if True:
            ##########spezial_word_path = self.get_input_file('Filepath to spezial words file: ')
            spezial_word_path = '/Users/lucienkaser/Desktop/spezial.txt'
            spezial_word_lines = self.file_to_list(spezial_word_path)
            spezial_word_lines = self.remove_double_words(spezial_word_lines)
            #self.print_all_lines_in_list(spezial_word_lines, 'Your spezial words: ')
            spezial_word_list = self.read_coordinates_from_line(spezial_word_lines)

            print('Spezal Words: ( ', len(spezial_word_list), ' )')
            for n in spezial_word_list:
                print(len(n), n)
        #returns the things
        return height, width, general_word_list, spezial_word_list

    #gets a number from the user
    def get_number_input(self, text):
        while True:
            try:
                data = int(input(text))
                print(data)
                print('You have entered: ', data)
                return data
            except:
                print('Invalid input')
    
    #removes double words:
    def remove_double_words(self, mylist):
        return list(dict.fromkeys(mylist))
    #gets a filepath from the user and checks if file exists
    def get_input_file(self, text):
        while True:
            data = input(text)
            if (os.path.isfile(data)):
                print('Input: ', data)
                return data
            else:
                print('selected file does not exist')

    #read all lines in file to list
    def file_to_list(self, filepath):
        list = []
        with open(filepath) as f:
            list = f.readlines()
        filtered_list = []
        for element in list:
            filtered_list.append(element.strip())
        return filtered_list

    #prints all lines in list
    def print_all_lines_in_list(self, list, leading_text):
        print(leading_text, '( ', len(list), ' )')
        for n in list:
            print('- ',n)

    #interpretes the spezial word lines
    def read_coordinates_from_line(self, line):
        list = [[]]
        for l in line:
            #print(' - '.join(str(l).split(',')))
            list.append(str(l).split(','))

        filteredlist = []
        for l in list:
            if(len(l) == 3):
                filteredlist.append(l)
        return filteredlist

    #askes the user a question with two possibilities
    def yes_no_Question(self, question, true_condition, false_condition):
        while True:
            values = [question, '(', true_condition, '/', false_condition, ')']
            data = input(''.join(values))
            if data.lower() == true_condition:
                return True
            elif data.lower() == false_condition:
                return False
            print('Invalid input')