class DataOutput:
    def __init__(self):
        print("init DataOutput")

    def process(self, solution, caps, wordpuzzle):
        self.write_file(solution, 'solution.txt')
        self.print_file(solution, 'solution.txt')
        self.write_file(caps, 'solution_capslock.txt')
        self.print_file(caps, 'solution_capslock.txt')
        self.write_file(wordpuzzle, 'wordpuzzle.txt')
        self.print_file(wordpuzzle, 'wordpuzzle.txt')
        print('printing fields')


    def write_file(self, field, name):
        with open(name, 'w') as file:
            for line in field:
                file.write(''.join(line) + '\n')
        
    def print_file(self, field, name):
        for line in field:
            print(''.join(line))