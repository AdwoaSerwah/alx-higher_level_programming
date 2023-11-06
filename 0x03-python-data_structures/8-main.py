#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
new = ""
my_new, new1 = multiple_returns(new)
print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(my_new, new1))
