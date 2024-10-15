import filecmp
 
f1 = "C:/Users/user/Documents/intro.txt"
f2 = "C:/Users/user/Desktop/intro1.txt"
 
# shallow comparison
result = filecmp.cmp(f1, f2)
print(result)
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
