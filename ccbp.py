import re
def ModifyString(s):
    w = re.split('(\d+)',s)
    numbers = []
    for word in w:
       if word.isdigit():
          numbers.append(int(word))
    numbers = sorted(numbers)
    print(numbers)
    k=0
    s=""
    for r in range(0,len(w)):
       if w[r].isdigit():
          w[r] = numbers[k]
          k=k+1;
       s = s+str(w[r]   )
    return(s)
s = "At 12pm total score is 180 with 8 4s 7 6s in 150 balls."
w = ModifyString(s)
print("Original String: %s"%s)
print("Modified String: %s"%w)
s = "I am 5 years 11 months and 8 days old."
w = ModifyString(s)
print("\nOriginal String: %s"%s)
print("Modified String: %s"%w)