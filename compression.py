from bitstring import BitArray
import os
import json

#NodeTree class to create Huffman Tree.

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

# For Compressed Files

def open_decode(filename: str):
    with open(filename, 'rb') as f:
        b = BitArray(f.read())
    binary = b.bin
    #binary = binary.strip('0')
    #print('b =', binary)
    return binary

def write_to_file(dictionary: dict[chr,str], txt_lines: list[str], filename: str):
    binary_string = ''
    for line in txt_lines:
        for character in line:
            binary_string = binary_string+dictionary[character]
    a = BitArray(bin=binary_string)
    with open(filename, 'wb') as f:
        a.tofile(f)

# For Text Files

def open_file(filename: str):
    txt_lines = []
    txt_lines = open(filename).readlines()
    return txt_lines

def write_txt(filename: str, text: str):
    with open(filename, 'w') as f:
        f.write(text)

# Find the number of occurrences (frequency) for each character in the text.
# Generates a dictionary of how many times a charecter is used.
        
def get_character_freq(txt_lines: list[str])-> dict[chr,int]:
    letter_freq = {}
    for line in txt_lines:
        for character in line:
            if character in letter_freq:
                letter_freq[character] += 1
            else:
                letter_freq[character] = 1
    return letter_freq

# Creates the huffman tree 

def huffman_code_tree(node, left: bool = True, binString: str =""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Uses the Huffman Code dictionary to decode the encoded file.

def huffman_decode(dictionary: dict, text: str):
    reversed_dict = {}
    for value, key in dictionary.items():
        reversed_dict[key] = value
    start_index = 0
    end_index = 1
    max_index = len(text)-1
    s = ''
    #print(reversed_dict)
    looper = True

    while looper == True:
        if text[start_index : end_index] in reversed_dict:
            s += reversed_dict[text[start_index : end_index]]
            start_index = end_index
        end_index += 1
        if start_index > max_index:
            looper = False
        elif end_index > max_index + 8:
            looper = False
        #print("start_index = " + str(start_index) + " end_index =  " + str(end_index) + " max_index = " + str(max_index))

    return s[:-1]

# write the huffman tree to file
def write_tree(filename: str, dictionary: dict):
    with open(filename, 'w') as file:
        file.write(json.dumps(dictionary))

# read the huffman tree from file
def read_tree(filename: str):
    return json.load(open(filename))

# when option 1 is selected

def encode():
    print("Please enter the name of your .txt file.")
    print("For example, if you wanted to encode 'test.txt' you would enter: 'test'.")
    print("")
    #take user input
    filename = input()

    
    lines = []
    lines = open_file(filename+".txt")

    print("File '" + filename + ".txt' has been succesfully found.")

    letter_freq = {}
    letter_freq = get_character_freq(lines)

    sorted_letter_freq = {}
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

    print("Letter frequency of text file '" + filename + ".txt' calculated.")

    nodes = sorted_letter_freq
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    print("Huffman Tree has been created.")

    huffman_code = huffman_code_tree(nodes[0][0])

    print("Compressing file.")

    write_to_file(huffman_code, lines, filename+".bin")
    write_tree(filename+".hufftree", huffman_code)

    return ("File '" + filename + ".txt' has been succesfully compressed to " + filename + ".bin. In addition, the huffman tree has been saved as " + filename + ".hufftree.")

# when option 2 is selected

def decode():
    print("Please enter the name of your compressed .bin file.")
    print("For example, if you wanted to uncompress 'test.bin' you would enter: 'test'.")
    print("")
    #take user input
    filename = input()
    hufffilename = filename
    
    encoded = open_decode(filename+".bin")

    print("If the name of the huffman tree you wish to use is not the same as the name of the file, please enter '1', any other input will use " + filename + ".hufftree.")
    user_input = input()
    if user_input == "1":
        print("Please enter the name of the .hufftree file.")
        hufffilename = input()

    huffman_code = read_tree(hufffilename+".hufftree")

    decoded = huffman_decode(huffman_code, encoded)

    write_txt(filename+"_decoded.txt", decoded)

    return ("File '" + filename + "_decoded.txt' has been succesfully decompressed from " + filename + ".bin using the huffman tree " + hufffilename + ".hufftree.")

def diff_hufftree():
    print("THIS FEATURE IS FOR EXPERIMENTING WITH USING DIFFERENT HUFFMAN TREES WITH .txt FILES.")
    print("THIS FEATURE MAY NOT WORK IF THE TREE DOESN'T CONTAIN THE SAME CHARACTERS.")
    print("")
    print("Please enter the name of your .txt file.")
    print("For example, if you wanted to encode 'test.txt' you would enter: 'test'.")
    print("")
    #take user input
    filename = input()
    
    lines = []
    lines = open_file(filename+".txt")

    print("File '" + filename + ".txt' has been succesfully found.")
    print("Please enter the name of the .hufftree file.")
    hufffilename = input()
    huffman_code = read_tree(hufffilename+".hufftree")
    print(huffman_code)

    write_to_file(huffman_code, lines, filename+"_"+hufffilename+".bin")

    return ("File '" + filename + ".txt' has been succesfully compressed to " + filename + "_" + hufffilename + ".bin using the huffman tree " + hufffilename + ".hufftree.")

cmd = 'mode 157,40'
os.system(cmd)
clear = lambda: os.system('cls')

quitter = False
error_message = ""


while quitter == False:
    print("""

   _____ _                       _        _____                          _____            _                                                           
  / ____(_)                     ( )      / ____|                        / ____|          | |                                                          
 | (___  _ _ __ ___   ___  _ __ |/ ___  | (___  _   _ _ __   ___ _ __  | |     ___   ___ | |                                                          
  \___ \| | '_ ` _ \ / _ \| '_ \  / __|  \___ \| | | | '_ \ / _ | '__| | |    / _ \ / _ \| |                                                          
  ____) | | | | | | | (_) | | | | \__ \  ____) | |_| | |_) |  __| |    | |___| (_) | (_) | |                                                          
 |_____/|_|_| |_| |_|\___/|_| |_| |___/ |_____/ \__,_| .__/ \___|_|     \_____\___/ \___/|_|                                                          
  _    _        __  __                          _____| |                                    _               _____                                     
 | |  | |      / _|/ _|                        / ____|_|                                   (_)             |  __ \                                    
 | |__| |_   _| |_| |_ _ __ ___   __ _ _ __   | |     ___  _ __ ___  _ __  _ __ ___ ___ ___ _  ___  _ __   | |__) _ __ ___   __ _ _ __ __ _ _ __ ___  
 |  __  | | | |  _|  _| '_ ` _ \ / _` | '_ \  | |    / _ \| '_ ` _ \| '_ \| '__/ _ / __/ __| |/ _ \| '_ \  |  ___| '__/ _ \ / _` | '__/ _` | '_ ` _ \ 
 | |  | | |_| | | | | | | | | | | (_| | | | | | |___| (_) | | | | | | |_) | | |  __\__ \__ | | (_) | | | | | |   | | | (_) | (_| | | | (_| | | | | | |
 |_|  |_|\__,_|_| |_| |_| |_| |_|\__,_|_| |_|  \_____\___/|_| |_| |_| .__/|_|  \___|___|___|_|\___/|_| |_| |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|
                                                                    | |                                                      __/ |                    
                                                                    |_|                                                     |___/

""")
    print(error_message)
    print("")
    print("What would you like to do?")
    print("1. Encode a .txt file.")
    print("2. Decode an encoded .bin file.")
    print("3. Encode a .txt using a different .hufftree file.")
    print("q. Quit.")
    user_input = input()
    if user_input == "1":
        error_message = ""
        clear()
        try:
            error_message = encode()
        except Exception as e:
            error_message = "ERROR: " + str(e)
    elif user_input == "2":
        error_message = ""
        clear()
        try:
            error_message = decode()
        except Exception as e:
            error_message = "ERROR: " + str(e)
    elif user_input == "3":
        error_message = ""
        clear()
        try:
            error_message = diff_hufftree()
        except KeyError as e:
            error_message = "ERROR: HUFFMAN TREE DOES NOT CONTAIN " + str(e) + "."
        except Exception as e:
            error_message = "ERROR: " + str(e)
    elif user_input == "q":
        quitter = True
    else:
        error_message = "Invalid input, please try again..."
    clear()





