#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
# my_list.app()
lst = MyList()
lst.print_sorted()
print(lst)
lst.append(-1)
lst.append(3)
lst.append(-2)
lst.print_sorted()

lst1 = MyList()
lst1.append(-2)
lst1.append(-7)
lst1.append(-5)
lst1.print_sorted()
