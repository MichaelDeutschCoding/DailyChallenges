import re

def reorder_matrix(matrix):
    # Takes in Matrix and returns one single string
    lst = matrix.split('\n')
    s = ""
    for i in range(len(lst[0])):
        for row in lst:
            s += row[i]
    return s

def read_clean_matrix(matr):
    # Removes non-alphanumeric characters and replaces them with a space.
    s = reorder_matrix(matr)
    # print('before regex', s)
    pat = re.compile(r'\W+')
    s = pat.sub(' ', s)
    # print('after regex', s)
    return s


text = """7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!"""

print("This is probably not exactly what you want it to look like, but this is exactly what you asked for!")
print(read_clean_matrix(text))