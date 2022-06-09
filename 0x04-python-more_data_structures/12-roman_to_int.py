#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    A function that converts a Roman numeral to an integer
    """
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'D': 500,
                  'M': 1000, 'L': 50, 'C': 100}
    roman_list = list(roman_string.upper())
    result = 0
    prev = 0
    for letter in roman_list:
        if letter in roman_dict:
            result += roman_dict[letter]
            if roman_dict[letter] > prev:
                result -= prev * 2
            prev = roman_dict[letter]
        else:
            return (0)
    return (result)
