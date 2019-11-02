import os
import sys
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def compress_me(file_path):
    old_size = os.stat(file_path).st_size
    picture = Image.open(file_path)
    dim = picture.size
    file = file_path[len(file_path) - file_path[::-1].find('/'):]
    picture.save(file_path[:len(file_path) - file_path[::-1].find('/')] + "/Compressed_" + file, "JPEG", optimize=True,
                 quality=10)
    new_size = os.stat(file_path[:len(file_path) - file_path[::-1].find('/')] + "/Compressed_" + file).st_size
    percent = ((old_size - new_size) / old_size) * 100
    print("File compressed from {}KB to {}KB or {}%".format(old_size / 1000, new_size / 1000, percent))
    return percent


def main():
    file_path = '/Users/raunit_x/Desktop/comedian.jpg'
    file = file_path[len(file_path) - file_path[::-1].find('/'):]
    compress_me(file_path)
    old_size = os.stat(file_path).st_size
    new_size = os.stat(file_path[:len(file_path) - file_path[::-1].find('/')] + "/Compressed_" + file).st_size
    original_image = mpimg.imread(file_path)
    compressed_image = mpimg.imread(file_path[:len(file_path) - file_path[::-1].find('/')] + "/Compressed_" + file)
    plt.title('ORIGINAL IMAGE: {}KB'.format(old_size / 1000))
    plt.imshow(original_image)
    plt.colorbar()
    plt.show()
    plt.title('COMPRESSED IMAGE: {}KB'.format(new_size / 1000))
    plt.imshow(compressed_image)
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    main()
