class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]

        self.d = {

            "d2r" : set(door, deer....)

        }

        """
        self.d = {}
        for w in dictionary:
            if not w: continue
            if len(w) <= 2:
                self.d.setdefault(w, set()).add(w)
            else:
                ab = w[0] + str(len(w) - 2) + w[-1]
                self.d.setdefault(ab, set()).add(w)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if len(word) <= 2:
            ab = word
        else:
            ab = word[0] + str(len(word) - 2) + word[-1]
        if ab in self.d:
            if word in self.d[ab] and len(self.d[ab]) == 1:
                return True
            else:
                return False
        else:
            return True

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)