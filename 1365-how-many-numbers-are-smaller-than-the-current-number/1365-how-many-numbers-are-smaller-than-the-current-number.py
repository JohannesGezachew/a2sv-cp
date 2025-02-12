class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        holder = sorted(nums)
        result = []
        dic = {holder[0]:0}
        count  = 0
        temp = 1
        for i in range(1,len(holder)):
            if holder[i] != holder[i-1]:
                if temp == 1:
                    count += 1
                else:
                    count += temp
                    temp = 1
                dic[holder[i]] = count
                    
            else:
                dic[holder[i]] = count
                temp += 1
        for num in nums:
            result.append(dic[num])
        
        return result

    
                

