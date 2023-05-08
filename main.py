# Exercise 1

def create_file(names):  # I couldn't call it names.txt as it raises an error
    with open(names, 'w') as file:
        file.write('Ada,Alan,Isabella,Lizbeth,Abigail,Meltem,Gülcan,Anna,Jonas,Max,Moritz')


create_file('names.txt')


# Exercise 2

def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as input:
        file = input.read()  # reading the file
        read = file.replace(',', '\n')  # replacing the comma with newline
    with open(output_file, 'w') as output:
        output.write(read)  # writing the replaced thing into new file


transform_to_row('names.txt', 'pretty_names.txt')


# Exercise 3

def add_greeting(input_file, output_file):
    with open(input_file, 'r') as input:  # opening it to update, as I need to read and write sth into it
        read = input.readlines()  # have to do it in a list to be able to iterate through it
    # adding Hello in the front using a for loop iterating through every index of the list
    add = []
    for i in read:
        greeting = 'Hello ' + i
        add.append(greeting)
    with open(output_file, 'w') as output:
        output.writelines(add)  # writing the list into a new file


add_greeting('pretty_names.txt', 'greeting_names.txt')


# Exercise 4

def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as input:
        read = input.read()
        rep = read.replace('Hello ', '')  # have to use the replace function
        # with using strip it would change the names as well
    with open(output_file, 'w') as output:
        output.write(rep)


strip_greeting('greeting_names.txt', 'strip_greeting.txt')


# Exercise 5

def combine_files(file1, file2, output_file):
    with open(file1, 'r') as file1:
        read1 = file1.readlines()  # to merge the lines I will have to read it in form of a list
    with open(file2, 'r') as file2:
        read2 = file2.readlines()

    merge = []  # creating empty list to add both lines into
    for file_1, file_2 in zip(read1, read2):  # looping through both files using zip function to pair the first lines of each
        # file together
        merge.append(file_1.strip('\n') + ' ' + file_2)  # removing the newline and adding them in one line

    with open(output_file, 'w') as output:
        output.writelines(merge)


combine_files('greeting_names.txt', 'strip_greeting.txt', 'combined.txt')
