class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        term_a = [100001 for i in range(len(s))] # aaabbbbbb(begins with a)
        term_b = [100001 for i in range(len(s))] # bbbbbbbbb(just with b)

        for j in range(len(s)-1, -1, -1):
            if j == (len(s)-1):
                if s[j] == 'a':
                    term_a[j] = 0
                    term_b[j] = 1
                else:
                    term_a[j] = 100001
                    term_b[j] = 0
            else:
                if s[j] == 'a':
                    term_a[j] = min(term_a[j+1], term_b[j+1])
                    term_b[j] = min(100001, 1 + term_b[j+1])
                else:
                    term_a[j] = min(1 + term_a[j+1], 100001)
                    term_b[j] = min(100001, term_b[j+1])

        return min(term_a[0], term_b[0])
