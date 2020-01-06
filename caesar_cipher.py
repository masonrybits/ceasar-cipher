import nltk
from nltk.corpus import words
word_list = words.words()
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(words, key):
    encrypted_words = ''

    for char in words.lower():
        if char in alphabet:
            encrypted_letter = alphabet[(alphabet.index(char.lower()) + key) % len(alphabet)]
            encrypted_words += encrypted_letter
        else:
            encrypted_words += char
    return encrypted_words

def decrypt(words):

    def english_words(list_of_words):
        number_correct = 0
        for word in list_of_words:
            if word in word_list:
                number_correct += 1
        if number_correct/len(list_of_words) >= 0.5:
            return True
        return False

    for key in range(len(alphabet)):
        a = encrypt(words, (-1*(key)))
        b = english_words(a.split(' '))
        if b:
            return a
