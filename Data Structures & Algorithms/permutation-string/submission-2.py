class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hashmap = dict()

        if len(s2) < len(s1):
            return False

        for n in s1:
            hashmap[n] = hashmap.get(n, 0) + 1

        for i in range(len(s1)):
            if s2[i] in hashmap:
                hashmap[s2[i]] -= 1

        if all(count == 0 for count in hashmap.values()):
            return True

        left = 0
        right = len(s1) - 1

        if s2[right] in hashmap:
            hashmap[s2[right]] += 1

        while right < len(s2):
            print(hashmap)

            if s2[right] in hashmap:
                hashmap[s2[right]] -= 1

            if all([num == 0 for num in hashmap.values()]):
                return True

            if s2[left] in hashmap:
                hashmap[s2[left]] += 1
            
            left += 1
            right += 1

        return False
