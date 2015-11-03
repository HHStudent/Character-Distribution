"""
distribution.py
Author: Dimitri
Credit: Sawyer

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
s = str(input("Please enter a string of text (the bigger the better): "))

print('The distribution of characters in "{0}" is:'.format(s))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s1 = s.lower().strip('.')
list1 = []
list2 = []

for x in alphabet:
    n1 = s1.count(x)
    list1.append(n1)

ziplist = list(zip(list1, alphabet))
length = len(s1)

while length > 0:
    for x in ziplist:
        if x[0] == length:
            list2.append(x[1]*x[0])
    length -= 1

for x in list2:
    print(x)