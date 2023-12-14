import random

def generate_random_word(consonants, vowels, min_length, max_length):
    word = ""
    length = random.randint(min_length, max_length)

    syllable_structures = [
        ['C', 'V'],
        ['C', 'V', 'C']
    ]

    for _ in range(length):
        chosen_structure = random.choice(syllable_structures)
        word += generate_syllable(consonants, vowels, chosen_structure)

    return word.capitalize()

def generate_syllable(consonants, vowels, syllable_structure):
    syllable = ""
    for s in syllable_structure:
        if s == 'C':
            syllable += random.choice(consonants)
        elif s == 'V':
            syllable += random.choice(vowels)

    return syllable

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

min_length = 1
max_length = 3
num_words = 5

random_words = [generate_random_word(consonants, vowels, min_length, max_length) for _ in range(num_words)]
print("Random Words:", random_words)
