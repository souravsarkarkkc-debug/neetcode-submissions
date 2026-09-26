class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        required = {}

        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        # 1. Build both frequency dictionaries completely
        for i in range(m):
            required[s1[i]] = required.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        # 2. Check the first complete window
        if required == window:
            return True

        # 3. Slide through the remaining windows
        for right in range(m, n):
            incoming = s2[right]
            window[incoming] = window.get(incoming, 0) + 1

            outgoing = s2[right - m]
            window[outgoing] -= 1

            if window[outgoing] == 0:
                del window[outgoing]

            if required == window:
                return True

        # 4. No matching window was found
        return False