class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list = s.split()
        if (list):
            return len(list[-1])
        return 0
