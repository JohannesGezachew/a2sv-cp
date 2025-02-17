class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        holder = [0] * (len(s)+1)
        nums =[]
        st = []

        for l, r, d in shifts:
            holder[l] += -1 if d == 0 else 1
            holder[r+1] += 1 if d == 0 else -1
         
        for i in range(1,len(holder)):
            holder[i] += holder[i-1]
        print(holder)
          
        for j in s:
           nums.append( ord(j))
        for h in range(len(nums)):
            nums[h] += holder[h]
        
        for num in range(len(nums)):
            nums[num] = (nums[num] - 97) % 26 + 97
        
        for num in nums:
            st.append(chr(num))
        return "".join(st)

