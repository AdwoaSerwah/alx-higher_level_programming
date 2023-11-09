#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_val_sks = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    int_num = 0
    prev_val_sk = 0
    for c in roman_string[::-1]:
        val_sk = roman_val_sks[c]
        if val_sk < prev_val_sk:
            int_num -= val_sk
        else:
            int_num += val_sk
        prev_val_sk = val_sk
    return int_num
