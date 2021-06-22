class DataOutput:
    def __init__(self):
        print("init DataOutput")

    #prints the given word puzzles into a file and into the console
    def process(self, solution, caps, wordpuzzle):
        self.write_file(solution, 'solution.txt')
        self.print_file(solution)
        self.write_file(caps, 'solution_capslock.txt')
        self.print_file(caps)
        self.write_file(wordpuzzle, 'wordpuzzle.txt')
        self.print_file(wordpuzzle)
        print('printing fields')
    #writes all lines of field into a file, with the name name
    def write_file(self, field, name):
        with open(name, 'w') as file:
            for line in field:
                file.write(''.join(line) + '\n')
    #prints all lines of field into the console
    def print_file(self, field):
        for line in field:
            print(''.join(line))