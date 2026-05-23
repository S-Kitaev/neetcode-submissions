class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # go throw the s with 2 pointers

        # add chars in hashmap if sum vals - k =< most freq val  -> sum += 1
        # else move left pointer to first char not same left, go on till right < len(s)

        max_l = 0
        curr_l = 0

        hashmap = dict()

        left = 0
        right = 0

        while right < len(s):

            if left == right:
                hashmap[s[left]] = 1
                curr_l = 1
                right += 1

            else:
                # hashmap[s[right]] = hashmap.get(s[right], 0) + 1
                # adding
                if sum(hashmap.values()) - k <= max(hashmap.values()):
                    hashmap[s[right]] = hashmap.get(s[right], 0) + 1
                    curr_l += 1
                    right += 1
                # deleting
                else:
                    if hashmap[s[left]] == 1:
                        del hashmap[s[left]]
                    elif hashmap[s[left]] > 1:
                        hashmap[s[left]] -= 1
                    curr_l -= 1
                    left += 1

            print(left, right)
            print(hashmap)
            if curr_l - max(hashmap.values()) <= k:
                max_l = max(max_l, curr_l)
        
        return max_l
        