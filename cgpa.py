
ct1 = float(input("Enter your ct1 marks: "))
ct2 = float(input("Enter your ct2 marks: "))
mid = float(input("Enter your mid marks: "))
atd = float(input("Enter your attendance marks: "))
obs = float(input("Enter your observation marks: "))
pct = float(60 / 40)

result = str((ct1 + ct2) * pct + mid + atd + obs)
result_2 = 300 - float(result)

print("your incourse marks is " + result)
print("your need minimum " + str(result_2) + " for A+.")