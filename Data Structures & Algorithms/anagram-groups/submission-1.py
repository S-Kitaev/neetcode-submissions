class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        string = {
            "a": 0,"b": 0,"c": 0,"d": 0,"e": 0,
            "f": 0,"g": 0,"h": 0,"i": 0,"j": 0,
            "k": 0,"l": 0,"m": 0,"n": 0,"o": 0,
            "p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"": 0,
            "u": 0,"v": 0,"w": 0,"x": 0,"y": 0,"z": 0,
        }

        hashmap = dict()

        for word in strs:
            counter = string.copy()

            for char in word:
                counter[char] += 1

            if tuple(counter.values()) in hashmap:
                hashmap[tuple(counter.values())].append(word)
            else:
                hashmap[tuple(counter.values())] = [word]

        return list(hashmap.values())

                