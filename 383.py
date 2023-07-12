"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        letters = collections.Counter(magazine)

        for c in ransomNote:
            if letters[c] <= 0:
                return False

            letters[c] -= 1

        return True
