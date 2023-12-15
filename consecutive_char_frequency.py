# frequency of consecutive same characters in a string 

""" 
    input: 
        list = "aaabbbaabbcccc" 
    output: "3a3b2a2b4c"
    
    input: 
        list = "pythonprogramming" 
    output: "1p1y1t1h1o1n1p1r1o1g1r1a2m1i1n1g"
    
    input: 
        list = "ccccaabaac"  
    output: "4c2a1b2a1c"

"""

input_string = "ccccaabaac"
n = len(input_string)

output_string=""
count = 1
for i in range(n-1):
    if input_string[i] == input_string[i+1]:
        count += 1
    else:
        output_string += str(count) + input_string[i]
        count = 1
output_string += str(count) + input_string[i+1]
print(output_string)