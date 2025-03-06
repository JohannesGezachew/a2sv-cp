class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        holder = defaultdict(lambda: -1)
        stack = []
        res = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                x = stack.pop() 
                holder[x] = nums2[i]
            stack.append(nums2[i])

            
        for num in nums1:
            res.append(holder[num])
        return res 