class Solution:
    def isValid(self, s: str) -> bool:
        opener = ['(','{','[']
        stack = []
        count = 0
        for c in s:
            if c in opener:
                stack.append(c)
                count +=1
                continue
            elif len(stack) == 0:
                return False
            else:
                back = stack[count - 1]
                if back == '(' and c == ')':
                    count -=1
                    stack.pop()
                elif back == '{' and c == '}':
                    count -=1
                    stack.pop()
                elif back == '[' and c == ']':
                    count -=1
                    stack.pop()
                else:
                    return False
        return len(stack) == 0