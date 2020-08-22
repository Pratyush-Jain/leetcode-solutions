class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if word[1:].lower() == word[1:]:
            return True
        else:
            return False
