class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        curr = 60 * int(time[:2]) + int(time[3:])
        digits = [int(x) for x in time if x != ':']
        digits.sort()
        new = curr
        while True:
            # Modulo will set it to zero if it crosses maximum time
            maxtime = 24 * 60
            new = (new + 1) % maxtime
            # Converting to minutes and hours
            new_hour = new / 60
            if new_hour < 10:
                new_hour = '0' + str(new_hour)

            new_minutes = new % 60
            if new_minutes < 10:
                new_minutes = '0' + str(new_minutes)

            new_digits = []
            # Extracting Digits from this
            new_digits += [int(x) for x in str(new_hour)]
            new_digits += [int(x) for x in str(new_minutes)]
            # print new_digits
            flag = True
            for d in new_digits:
                if len(new_digits) < 4 or d not in digits:
                    flag = False

            if flag:
                return str(new_hour) + ':' + str(new_minutes)