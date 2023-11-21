from typing import List

def isAcronym(words: List[str], s: str) -> bool:
    
    if len(s)!= len(words):
        return False
    
    for i in range(len(s)):
        if s[i]!= words[i][0]:
            return False
        
    return  True


words = ["alice","bob","charlie"]
s = "abc"
print(isAcronym(words, s))