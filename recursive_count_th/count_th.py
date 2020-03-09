'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# slice through the array recursively checking for 't' and 'h' until there is 1 character left

def count_th(word):
    if len(word) < 2:
        return 0
    elif word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

print('count this ' + str(count_th('this')))
print('empty '+ str(count_th('')))
print('wordth '+ str(count_th('wordth')))
