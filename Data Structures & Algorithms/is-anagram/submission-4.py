class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()

        if len(s) > len(t):
            bigger = s
            lower = t
        else:
            bigger = t
            lower = s

        for i in range(len(bigger)):
            hashmap[bigger[i]] = hashmap.get(bigger[i], 0) + 1

        for i in range(len(lower)):
            if lower[i] in hashmap:
                hashmap[lower[i]] -= 1

        if any(hashmap.values()) != 0:
            return False
        else:
            return True
        