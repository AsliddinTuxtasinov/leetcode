# 1832. Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, 
# return true if sentence is a pangram, or false otherwise.

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

def checkIfPangram(sentence: str) -> bool:
    english_alphabet="abcdefghijklmnopqrstuvwxyz"
    
    if len(sentence) < 26:
        return False
    
    sentence = "".join(map(str, sorted(set(sentence))))
    print(sentence)
    return sentence == english_alphabet


print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print("============")
print(checkIfPangram("leetcode"))
