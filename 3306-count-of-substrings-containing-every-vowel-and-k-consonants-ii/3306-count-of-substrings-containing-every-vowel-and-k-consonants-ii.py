class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeast(word, k) - self._atLeast(word, k + 1)
    
    def _atLeast(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        res = 0
        left = 0
        consonants = 0
        vowel_counts = defaultdict(int)
        
        for right, ch in enumerate(word):
            if ch in vowels:
                vowel_counts[ch] += 1
            else:
                consonants += 1
            
            while len(vowel_counts) == 5 and consonants >= k:
                res += n - right

                left_char = word[left]
                if left_char in vowels:
                    vowel_counts[left_char] -= 1
                    if vowel_counts[left_char] == 0:
                        del vowel_counts[left_char]
                else:
                    consonants -= 1
                left += 1
        
        return res