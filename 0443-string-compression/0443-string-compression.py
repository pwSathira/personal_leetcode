class Solution:
    def compress(self, chars: List[str]) -> int: 
        if not chars:
            return 0 # Or []

        output = []
        i = 0
        n = len(chars)
        while i < n:
            current_char = chars[i]
            count = 0
            # Count occurrences of current_char
            j = i
            while j < n and chars[j] == current_char:
                count += 1
                j += 1

            # Append the character
            output.append(current_char)

            # Append the count if it's greater than 1
            if count > 1:
                for digit in str(count): # "12" becomes "1", "2"
                    output.append(digit)
            
            i = j
        
        k = 0
        for char_to_write in output:
            if k < len(chars):
                chars[k] = char_to_write
            else: 
                chars.append(char_to_write) 
            k +=1
        return k 
