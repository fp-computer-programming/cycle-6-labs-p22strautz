# Author: SCT (AMDG) 11/12/21

subjects = ['calculus', 'language and compostion', 'u.s goverment']
print(subjects)

subjects.append('enviormental science')
print(subjects)

print(subjects.index('enviormental science'))

subjects.sort()
print(subjects)

more_subjects = subjects.copy()

more_subjects.reverse()
print(more_subjects)
print(subjects)
