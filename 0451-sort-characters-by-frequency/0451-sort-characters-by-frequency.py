class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        li = []
        for key,value in counter.items():
            li.append([value,key])
        li.sort(reverse= True)

        result = []
        for v,k in li:
            result.append(k *v)

        return "".join(result)