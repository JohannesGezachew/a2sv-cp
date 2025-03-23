class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list1 = [i for i in range(1,n+1)]
        left = 0
        temp = n
        while temp > 1 :
            index = ((left - 1 + k) % temp )
            temp -= 1
            list1.remove(list1[index])   

            left = index
        return list1[0]