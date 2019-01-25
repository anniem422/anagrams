def anagrams(word):
    result = []
    length = len(word)
    anagram = ''
    
    if length <= 1:
        result.append(word)
        return result
    
    else:
    
        for char in anagrams(word[1:]) :
            for element in range (length):
                anagram = char[:element]+ word[0:1]+ char[element:]
                #accounts for doubles 
                if anagram not in result:
                    result.append(anagram)
            
    return result
    
    

