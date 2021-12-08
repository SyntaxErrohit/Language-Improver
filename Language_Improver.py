# Intro
print('LANGUAGE IMPROVER')
print('m- m- m- m- made by rohit elamurugan')
print()

# Input
print('Engwish goesh hewe...')
string = input()
print()

# Replacing s with sh
# I had to do like this because Beluga ignored words which already have "sh"
i = 0
temp = ''
while i < len(string):
    if string[i] == 's' and string[i+1] == ' ':
        temp += 'sh' + string[i+1]
        i += 2
    else:
        temp += string[i]
        i += 1
string = temp

# Replacing "r" and "l" with "w"
string = string.replace('r', 'w')
string = string.replace('l', 'w')

# Output
print('Youw impwoved engwish...')
print(string)
print()
