def decodeString_backward1(s):
    stack = []
    i = len(s) - 1  # Start from the end of the string

    while i >= 0:
        if s[i] == ']':
            # Push a marker to indicate the start of an encoded substring
            stack.append(']')
            i -= 1
        # for valid encodings, can skip elif s[i].isdigit(), because digits are associated with "[".
        elif s[i] == '[':  # decoding until top ']', and push decoding str to the stack
            # get repetition times(rep)
            i -= 1  # now are number digits
            num = ''
            while i >= 0 and s[i].isdigit():
                num = s[i] + num
                i -= 1
            rep = int(num) if num else 1  # Handle cases where num might be empty

            # get process_str to be repeated
            # process_str is in order
            process_str = ''
            while stack and stack[-1] != ']':
                process_str += stack.pop()

            # pop the top ']'
            if stack[-1] == ']':  # necessary condition?
                stack.pop()

            # repetition
            process_str = process_str * rep

            # push reversed process_str into stack(resemble backward scanning)
            # for ch in reversed(process_str):
            #     stack.append(ch)
            for j in reversed(range(len(process_str))):
                stack.append(process_str[j])
        else:
            # For letters, push onto the stack
            stack.append(s[i])
            i -= 1
    # Build the final result from the stack
    result = ''.join(stack[::-1])
    return result


result3=decodeString_backward1("3[ab]2[bc]")
print("correct method, result3 is ",result3) #abababbcbc
result4=decodeString_backward1("3[a2[cb]]")
print("correct method, result4 is ",result4) #acbcbacbcbacbcb