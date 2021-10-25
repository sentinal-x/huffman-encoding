# 'Simon's Super Cool Huffman Compression Program' Tool

## Introduction

Hello! Welcome to the README for 'Simon's Super Cool Huffman Compression Program'
compression tool. 

This tool allows users to compress .txt files into .bin files alongside creating
a .hufftree file which contains the Huffman Code of a given encoding. 

## Prerequisites

Python 3.9 was used for the development of this project. 

This project was developed for Windows and so may not work on MacOS or Linux.

## Installation and Requirements

You will need to install the 'bitstring' module using pip install. 

The pip install command for this is:

'pip install bitstring'

## Getting Started

To get started with the 'Simon's Super Cool Huffman Compression Program' tool,
simply run the 'compression.py' file, either from where you've stored the file or
from the Command Prompt - navigating to the folder using cd and executing the
command 'py compression.py'. 

You will be greeted with a main menu, from here you can select one of four
options: to encode a .txt file, to decode a compressed .bin file, to encode a
.txt file using a different .hufftree huffman code file, or simply just to
quit the program. Please note that the third option is purely for 
experimentation and may not work with a given .hufftree file, it will also not
produce as viable of a compression as with the first option.

For the sake of simplicity, place the .txt files you wish to compress in the
same folder as your 'compression.py' file. If you wish to compress a file in
another folder, just enter the full file location of the .txt file before the
filename. For example, by entering 'C:\Users\your_name\Documents\test' when 
prompted, program will compress test.txt in your Documents folder. The .bin 
files and .hufftree files should be accessed in the same manner.

## License

MIT License

Copyright (c) 2021 Simon James Puttock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.