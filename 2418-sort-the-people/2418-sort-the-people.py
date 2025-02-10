class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(heights)-1):
            min_index = i
            for j in range(i+1,len(heights)):
                if heights[j] > heights[min_index]:
                    min_index = j
            if i != min_index:
                 temp = heights[i]
                 heights[i] = heights[min_index]
                 heights[min_index] = temp

                 temp = names[i]
                 names[i] = names[min_index]
                 names[min_index] = temp
                
        return names