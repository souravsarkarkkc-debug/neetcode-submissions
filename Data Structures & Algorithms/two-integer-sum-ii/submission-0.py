class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2  = len(numbers)-1
        

        while index1<index2:
            total = numbers[index1]+numbers[index2]
            if target > total :
                index1 += 1
            elif target < total:
                index2 -= 1
            elif target == total:
                return[index1+1,index2+1]

