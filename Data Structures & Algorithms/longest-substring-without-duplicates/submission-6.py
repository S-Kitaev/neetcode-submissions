class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()

        left = 0
        right = 0
        answer = 0

        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        hashmap[s[right]] = 1

        while left < len(s) and right < len(s):

            if all([val == 1 for val in hashmap.values()]):
                answer = max(answer, right - left + 1)
                # right += 1
                # hashmap[s[right]] = hashmap.get(s[right], 0) + 1
                if right + 1 < len(s):
                    right += 1
                    hashmap[s[right]] = hashmap.get(s[right], 0) + 1
                else:
                    break
            else:
                if hashmap[s[left]] > 1:
                    hashmap[s[left]] = hashmap.get(s[left], 0) - 1
                elif hashmap[s[left]] == 1:
                    del hashmap[s[left]]
                left += 1
                answer = max(answer, right - left + 1)

        return answer