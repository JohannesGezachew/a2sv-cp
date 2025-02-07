class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter1 = {}
        dic = Counter()

        result  =[]


        for word in words1:
            counter1[word] = Counter(word)

        for w in words2:
                cw = Counter(w)
                for k,v in cw.items():
                    dic[k] = max(v, dic[k])
          
        for word in words1:
            if counter1[word] >= dic:
                result.append(word)

        return result





       