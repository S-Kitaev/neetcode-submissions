class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_list = []
        for i in range(len(s)):
            if s[i].isalpha():
                s_list.append(s[i].lower())
            elif s[i].isdigit():
                s_list.append(s[i])
        return s_list == s_list[::-1]
        