class Solution:
    def smallestSubsequence(self, s):
        last = {}

        # Find last occurrence of every character
        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()

        for i in range(len(s)):
            ch = s[i]

            # Already included
            if ch in seen:
                continue

            # Remove bigger characters if they appear again later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)