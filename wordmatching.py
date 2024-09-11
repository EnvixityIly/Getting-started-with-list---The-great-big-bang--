# Drake and diddy party
def match_word(words):
    
    count = 0
    lst = []

    for word in words:

        if len(word) > 1 and word[0] == word[-1]:
            count = count + 1
            lst.append(word)

        
    print("List of words with first and last character same/n", lst)
    return count

li = ['Diddy', 'aba', 'Racist', 'Minor', 'Drakes first love']

cnt = match_word(li)

print("Number of words having first and last character same are ",cnt)