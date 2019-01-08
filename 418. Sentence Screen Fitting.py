class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence)
        s += ' '
        l = len(s)
        start = 0
        for i in range(rows):
            start += cols
            # Decrease the start
            if s[start % l] == ' ':
                start += 1
            else:
                while start > 0 and s[(start - 1) % l] != ' ':
                    start -= 1

        return start / l



