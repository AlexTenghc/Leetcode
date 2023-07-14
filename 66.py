"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.""'
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mul = 1
        num = 0
        for i in range(len(digits)-1, 0, -1):
            num += digits[i] * mul
            mul *= 10
        num += digits[0] * mul

        num += 1
        output = []
        while num != 0:
            output.append(num%10)
            num = num // 10

        print(output)
        return output[::-1]
