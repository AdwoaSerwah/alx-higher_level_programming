#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'bag': {'app': "me", 'amt': 45}, 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
