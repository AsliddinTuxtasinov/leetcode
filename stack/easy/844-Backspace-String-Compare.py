class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for s_item in s:
            if s_item == '#':
                if len(s_stack) > 0:
                    s_stack.pop()
            else:
                s_stack.append(s_item)

        for t_item in t:
            if t_item == '#':
                if len(t_stack) > 0:
                    t_stack.pop()
            else:
                t_stack.append(t_item)

        return s_stack == t_stack


if __name__ == '__main__':
    s = "y#fo##f"
    t = "y#f#o##f"
    print(Solution().backspaceCompare(s, t))
