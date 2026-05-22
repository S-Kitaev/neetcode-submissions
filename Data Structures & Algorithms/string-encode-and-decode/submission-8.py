class Solution:

    def encode(self, strs: List[str]) -> str:

        new_strs = ""
        for word in strs:
            for char in word:

                new_strs += str(ord(char))
                new_strs += "."
            new_strs += "/"
        return new_strs
            

    def decode(self, s: str) -> List[str]:

        new_list = []
        old_list = s.split("/")[:-1]

        for word in old_list:
           word = word[:-1]
           word = word.split(".")
           word = [chr(int(char)) if char != '' else '' for char in word]
           word = "".join(word)
           new_list.append(word)

        return new_list
            
