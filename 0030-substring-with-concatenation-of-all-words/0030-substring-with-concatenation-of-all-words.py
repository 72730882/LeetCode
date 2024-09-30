class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return[]
        
        word_count = Counter(words)
        word_length = len(words[0])
        window_length = word_length * len(words)
        results = []

        for i in range(len(s) - window_length + 1):
            words_in_window = [s[j:j+word_length] for j in range(i, i+window_length, word_length)]
            word_count_in_window = Counter(words_in_window)

            if word_count == word_count_in_window:
                results.append(i)
        return (results)
        