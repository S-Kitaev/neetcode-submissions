class Solution:
    def reverseBits(self, n: int) -> int:

        zeros = '00000000000000000000000000000000'

        number = []

        while n > 0:
            char = n % 2
            number.append(str(char))
            n = n // 2
        
        s_num = "".join(number)
        # print(s_num)
        s_num = s_num + zeros
        s_num = s_num[::-1]
        s_num = s_num[-32:]

        result = 0
        # print(s_num)
        for i in range(len(s_num)):
            result += int(s_num[i]) * 2**i

        return result

        