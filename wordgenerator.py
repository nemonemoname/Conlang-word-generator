import random

def generate_random_word(consonants, vowels, syllable_structure, min_length, max_length):
    word = ""
    length = random.randint(min_length, max_length)

    for _ in range(length):
        syllable = generate_syllable(consonants, vowels, syllable_structure)
        word += syllable

    return word.capitalize()

def generate_syllable(consonants, vowels, syllable_structure):
    syllable = ""
    for s in syllable_structure:
        if s == 'C':
            syllable += random.choice(consonants)
        elif s == 'V':
            syllable += random.choice(vowels)
    return syllable

def generate_random_words(consonants, vowels, syllable_structure, min_length, max_length, num_words):
    words = [generate_random_word(consonants, vowels, syllable_structure, min_length, max_length) for _ in range(num_words)]
    return words

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z'] #Consonants
vowels = ['a', 'e', 'i', 'o', 'u'] #Vowels
syllable_structure = ['C', 'V']  # Consonant followed by Vowel

min_length = 3 #Minimum lengths of words
max_length = 8 #Max lengths of words
num_words = 5  # Adjust the number of words to generate

random_words = generate_random_words(consonants, vowels, syllable_structure, min_length, max_length, num_words)
print("Random Words:", random_words)
