import re # Regular Expressions
from collections import Counter
import string
from flask import Flask, render_template, request


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.readlines()
        words = []

    for line in text:
        words = words + re.findall(r'\w+', line.lower())  # RE for making a words list from file
    
    print(words, file=open("output.txt", "a"))
    return words

read_file('bible.txt')
