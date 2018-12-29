class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Backtracking Solution
        answer = []

        def generate(opening, closing, string):
            if opening == closing == n:
                answer.append(string)

            if opening < closing:
                # The string becomes invalid, hence backtrack
                return
            if opening >= closing and opening < n:
                generate(opening + 1, closing, string + '(')
                generate(opening, closing + 1, string + ')')

            if opening > closing and opening >= n:
                generate(opening, closing + 1, string + ')')

            return answer

        answer = generate(1, 0, '(')

        return answer



