class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                third = 0
                if token == '+':
                    third = first + second
                elif token == '-':
                    third = first - second
                elif token == '*':
                    third = first * second
                else:
                    third = first / second
                
                stack.append(int(third))
            
        return stack[-1]

s = Solution()

print(s.evalRPN(tokens = ["1","2","+","3","*","4","-"]))

#Explanation: ((1 + 2) * 3) - 4 = 5