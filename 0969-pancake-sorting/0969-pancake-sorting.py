class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []

        while n > 0:
            index = arr.index(n)
            if index != n - 1:
                arr = arr[index::-1] + arr[index+1:]
                result.append(index + 1)

                arr = arr[n-1::-1] + arr[n:]
                result.append(n)
            n -= 1

        return result
