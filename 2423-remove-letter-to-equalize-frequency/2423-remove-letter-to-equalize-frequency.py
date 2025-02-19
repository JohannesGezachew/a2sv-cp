class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(word) == len(set(word)):
            return True
        counter = Counter(word)
        comparator = int(counter[max(counter)])-1
        count = 0
        for w in word:
            if counter[w] > comparator:
                count += 1
                counter[w] -= 1
        return count <= 1
