# Author: SCT (AMDG) 11/12/21

colors = ['red', 'orange', 'yellow', 'green']
print(colors)

colors.extend(['blue', 'purple', 'indigo'])
print(colors)

print(colors.count('yellow'))

colors.insert(3, 'teal')
print(colors)

colors.clear()
print(colors)

print(colors.count('red'))
