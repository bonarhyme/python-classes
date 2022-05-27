# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    wordLower = word.lower()
    anagramLower = anagram.lower()

    if(len(wordLower) == len(anagramLower)):
        sortedWordLower = sorted(wordLower)
        sortedAnagramLower = sorted(anagramLower)

        if(sortedWordLower == sortedAnagramLower):
            return True
        else:
            return False

    else:
        return False

print(find_anagram("boye", "oeby"))