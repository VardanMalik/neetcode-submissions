class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] !="]":
                stack.append(s[i])
            else:
                subString = ""
                while stack[-1]!="[":
                    subString = stack.pop() +subString
                stack.pop() #remove opening bracket from stack
                number= ""
                while stack and stack[-1].isdigit():
                    number = stack.pop()+number
                stack.append(int(number)* subString)
        return "".join(stack)