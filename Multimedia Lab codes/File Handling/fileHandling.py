# Write a program to write and display the data in file.


def read_and_display_file(path):
    print("READING THE FILE: {}\n".format(path[len(path) - path[::-1].find('/'):]))
    with open(path, 'r') as file:
        data = file.readlines()
        for line in data:
            print('\t\t{}'.format(line))
    print("\n\nFILE IS READ AND NOW CLOSED\n")


def write_and_display_file(path):
    print("\n\nWRITING ON THE FILE: {}".format(path[len(path) - path[::-1].find('/'):]))
    text = "This is some custom text!"
    with open(path, 'a') as file:
        file.write(text)
    print("\n\n'{}' appended to the file".format(text))
    read_and_display_file(path)


if __name__ == '__main__':
    file_path = '/Users/raunit_x/Desktop/random.txt'
    read_and_display_file(file_path)
    write_and_display_file(file_path)



