s = 'abcabcbb'
count = 0
ss = list(s)
prev_ss = ss[0]#'a'
ss_value = prev_ss
print(ss)
print(substring for substring in ss[1:0])
for substring in ss[1:]:    #['a','b','c','b','c','b','b']
    print(f"{substring}")
    if substring in ss_value: 
        ss_value = prev_ss
        print("if", ss_value)
    else:
        ss_value += substring
        print("else",ss_value)
    prev_ss = substring
    output = ss_value
    
    print(">>>>>>>>>>>>>>>>prevss",prev_ss)
    print("output", ss_value, len(ss_value))
# return len(ss_value)
        
# output = lengthOfLongestSubstring('abcabcbb')
# print(output)