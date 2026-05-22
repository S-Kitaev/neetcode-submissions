class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mydict = dict()
        starts = []
        lenghts = []

        for num in nums:
            mydict[num] = None

        for i in nums:
            if i - 1 not in mydict:
                starts.append(i)
            else:
                mydict[i - 1] = i

        if len(starts) == 0:
            return 0

        for start in starts:

            lenght = 1
            curr_num = start

            while mydict[curr_num] is not None:
                curr_num = mydict[curr_num]
                lenght += 1

            lenghts.append(lenght)

        return max(lenghts)
        # return mydict
        # return starts

        
                

            

        
