class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        num = 0

        for char in s:
            if char.isdigit():
                # Build the number for repeat count
                num = num * 10 + int(char)
            elif char == "[":
                # Push the current context to stack
                stack.append((current_string, num))
                current_string = ""
                num = 0
            elif char == "]":
                # Pop and combine the repeated substring
                last_string, repeat_count = stack.pop()
                current_string = last_string + current_string * repeat_count
            else:
                # Append character to the current string
                current_string += char

        return current_string