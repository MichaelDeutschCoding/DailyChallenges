test_list = ['a', 'b', 'c']

substring_visualized = """
 - - -
 - - c
 - b -
 - b c
 a - -
 a - c
 a b -
 a b c
 """

def print_bin():
    for i in range(8):
        print(f'{i})  {i:03b}')

# print(substring_visualized)
# print_bin()


##### BINARY IMPLEMENTATION

# SHOW BINARY
# remove the '0b' prefix
def find_ones(num):
    binary = bin(num)[2:]
    ones_index = [i for i , value in enumerate(binary) if value == '1']
    # print('decimal:', num)
    # print('binary :', binary)
    # print('Indices of 1s:', ones_index)
    return ones_index

# find_ones(6)

def binary_implementation(array):
    results = []
    for i in range(2 ** len(array)):
        substring = []
        ones = find_ones(i)
        for index in ones:
            substring.append(array[index])
        results.append(substring)
    return results

### comment out print calls!
# print(binary_implementation(test_list))


#### CLEANER IMPLEMENTATION

def demonstrate_bitwise_and():
    print(f'{6:>2})  {6:04b}')
    print(f'{13})  {13:04b}')
    print(' ~~    ~~ ')
    print(f'{6 & 13:>2})  {4:04b}')

# demonstrate_bitwise_and()

def demonstrate_left_shift():
    print(f"0 left shifts: {1:04b}")
    print(f"1 left shift:  {1 << 1:04b}")
    print(f"2 left shifts: {1 << 2:04b}")
    print(f"3 left shifts: {1 << 3:04b}")

# demonstrate_left_shift()


def unique_subsets(array):
    results = []
    for i in range(2 **len(array)):
        subs = []
        for j in range(len(array)):
            if i & (1 << j):
                subs.append(array[j])
        results.append(subs)
    return results

# print(unique_subsets(test_list))


# print(unique_subsets([4,5,6]))
# print(unique_subsets([4,5,6,7]))