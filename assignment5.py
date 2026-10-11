#1
for i in range(2, 15, 3):
    print(i)
    #2,5,8,11,14

#2 
for i in range(15, 2, -3):
    print(i)
    #14,11,8,5,2
#3 
for i in range(4, 31, 5):
    print(i) 
    #4,9,14,19,24,29
# (how many iterations? -> 6)

#4
for i in range(3, 19, 3):
    print(i) 
#5  
for i in range(5,11,1):
    print(i,(20-i))
#6 
for i in range(1,7):
    print(i,i**2,i**3)
#7 
start=int(input("enter start:")) 
end=int(input("enter end:"))
sum=0     
for i in range(start,end+1):
 sum+=i
print(sum)
#8  
N=int(input("Enter N:"))
count=0
for i in range(1,N+1):
    if i%3==0:
     count+=1
print(count)
#9   
N=int(input("Enter N:"))
sum=0
for i in range(1,N+1):
    if i%4==0:
     sum+=i
print(sum) 
#10     
N=int(input("Enter N:"))
sum=0
for i in range(1,N+1):
    if i%3==0 and i%5==0:
     sum+=i
print(sum)
#11 
N=int(input("Enter N:"))
sum=0
for i in range(1,N+1):
    if i%3!=0:
     sum+=i
print(sum)
#12 
count_even=0
count_odd=0
N=int(input("enter a N:"))
for i in range(1,N+1):
   if i%2==0:
      count_even+=1
   else: 
      count_odd+=1
print("Even=",count_even,"Odd=",count_odd) 
#13 
N=int(input("Enter N:"))
sum=0
for i in range(1,N+1):
     sum+=i
     print(sum) 
#14 
N=int(input("Enter N:"))
factorial=1
for i in range(1,N+1):
     factorial*=i
     print(factorial) 
#15     
N=int(input("Enter N:"))
factorial=1
for i in range(1,N+1):
     factorial*=i
print(factorial)      
#16     
N=int(input("Enter N:"))
factorial=1
for i in range(1,N+1):
     factorial*=i
     print(i,"! =",factorial)
#17             
N=int(input("Enter N:"))
factorial=1
for i in range(1,N+1):
    if i%2==0:
     factorial*=i
print(factorial)                
#18             
N=int(input("Enter N:"))
factorial=1
for i in range(1,N+1):
    if i%2!=0:
     factorial*=i
print(factorial)       
#19             
N=int(input("Enter N:"))
factorial=1
for i in range(N,1,-1):
    if i%2==0:
     factorial*=i
print(factorial)
#20         
N=int(input("Enter N:"))
sum=0
for i in range(1,N+1):
     i**=2
     sum+=i
print(sum)          
#21             
N=int(input("Enter N:"))
sum=0
for i in range(1,N+1):
     i**=3
     sum+=i
print(sum)          
#22                                         
N=int(input("Enter N:"))
sum=0
factorial=1
for i in range(1,N+1):
    factorial*=i
    sum+=factorial
print(sum)  
#23 
num=int(input("enter a number:"))
count=0
import math 
for i in range(int(math.log10(num))+1):
   count+=1
print(count)
#24
import math

n = abs(int(input("Enter an integer: ")))
total = 0
for i in range(int(math.log10(n)+1)):
    total += n % 10
    n //= 10
print(total)
#25
import math

n = abs(int(input("Enter an integer: ")))
total = 1
for i in range(int(math.log10(n)+1)):
    total 
    total*= n % 10
    n //= 10
print(total)
#26
import math

n = abs(int(input("Enter an integer: ")))
count=0
for i in range(int(math.log10(n)+1)):
    digit= n % 10 
    
    if digit%2==0:
     count+=1
    n //= 10
print(count)
#27
import math

n = abs(int(input("Enter an integer: ")))
sum=0
for i in range(int(math.log10(n)+1)):
    digit= n % 10 
    
    if digit%2==0:
     sum+=digit
    n //= 10
print(sum)
#28         
import math

n = abs(int(input("Enter an integer: ")))
digits = int(math.log10(n)) + 1 

largest = 0
for i in range(digits):
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10              
print(largest)
#29
import math

n = abs(int(input("Enter an integer: ")))
digits = int(math.log10(n)) + 1 

smallest = 0
for i in range(digits):
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10              # outside the if, runs every pass
print(smallest)
#30
import math

n = abs(int(input("Enter an integer: ")))
digits = int(math.log10(n)) + 1 
reverse_number=""
for i in range(digits):
    last_digit= n % 10
    reverse_number+=str(last_digit)
    n=n//10 
                 
print(reverse_number)
#31
import math

n = abs(int(input("Enter an integer: ")))
original=n
digits = int(math.log10(n)) + 1 
reverse_number=""
for i in range(digits):
    last_digit= n % 10
    reverse_number+=str(last_digit)
    n=n//10 
print(reverse_number) 
d=int(reverse_number)   
if d==original:
        print("Palindrome")
else:
        print("Not Palindrome") 
#32
import math
n=abs(int(input("enter number")))   
target=int(input("enter target:")) 
digits=int(math.log10(n)+1)
for i in range(digits):
    last_digit=n%10
    n=n//10
    if target==last_digit:
     print("found!")
#33
import math

n = abs(int(input("Enter an integer: ")))
digits = int(math.log10(n)) + 1 
for i in range(digits):
    last_digit= n % 10
    n=n//10 
print(last_digit) 
#34
import math

n = abs(int(input("Enter an integer: ")))
digits = int(math.log10(n)) + 1 
largest=0
smallest=9
for i in range(digits):
    last_digit= n % 10
    if last_digit>largest:
        largest=last_digit
    if last_digit<=smallest :
        smallest=last_digit   
    n=n//10 
print(largest-smallest)
#35
import math 
n=int(input("enter n:"))
digit=int(math.log10(n))+1
for i in range(1,digit+1):
    last_digit=n%10
    n=n//10
    print(last_digit,i) 
#36
import math 
n=int(input("enter n:"))
original=n
digit=int(math.log10(n))+1
sum=0
for i in range(digit):
    last_digit=n%10
    sum+=last_digit**digit
    n//=10
if sum==original:
        print("Armstrong Number")
else:
        print("Not Armstrong Number")  
#37
string=input("enter a string:")
for i in range(len(string)):
    print(i,string[i]) 
#38
s = input("Enter a string: ")

count = 0
for ch in s:
    count += 1
print(count)
#39
s = input("Enter a string: ")
consonants=0
vowels= 0
for ch in s:
    if ch in "aeiou":
        vowels+=1
    elif ch!=" ":
        consonants+=1    
print("vowels:",vowels)
print("consotants:",consonants) 
#40
s = input("Enter a string: ")
target=input("enter target:")
count=0
for ch in len(s):
    if ch==target:
        count+=1
print(count) 
#41
s = input("Enter a string: ")
target=input("enter target:")
position=-1
for i in range(len(s)-1,-1 ,-1):
    if s[i]==target :
        position=i
if position==-1:
   print("Not Found") 
else:
    print(position) 
#42
s = input("Enter a string: ")

upper = 0
lower = 0
for ch in s:
    if "A" <= ch <= "Z":
        upper += 1
    elif "a" <= ch <= "z":
        lower += 1
print(f"Uppercase = {upper}, Lowercase = {lower}")  
#or
s = input("Enter a string: ")

upper = 0
lower = 0
for ch in s:
    code = ord(ch)
    if 65 <= code <= 90:
        upper += 1
    elif 97 <= code <= 122:
        lower += 1
print(f"Uppercase = {upper}, Lowercase = {lower}")
#43
s = input("Enter a string: ")
for ch in s:
     code = ord(ch)
     print(ch,code)  
#44
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch.lower() not in "aeiou":
        result += ch
print(result) 
#or
s = input("Enter a string: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

result = ""
for ch in s:
    if ch not in vowels:
        result += ch
print(result)
# Level 6 — Midpoint, Half & String Logic
#45
s = input("Enter a string: ")
mid = int(len(s) / 2)
print(s[mid])
#Using a for loop
s = input("Enter a string: ")
mid = len(s) // 2

for i, ch in enumerate(s):
    if i == mid:
        print(ch)
#46
s = input("Enter a string: ")
mid = len(s) // 2

for i, ch in enumerate(s):
    if i< mid:
        print("First Half :",ch) 
    else:
        print("Second Half :",ch)
#47
s = input("Enter a string: ")
mid = len(s) // 2
first = ""
second = ""
for i, ch in enumerate(s):
    if i< mid:
        first+=ch   
    else:
        second+=ch
print("First Half :", first)
print("Second Half :", second)
#47
s = input("Enter a string: ")
mid = len(s) // 2
first = ""
middle=""
second = ""
for i, ch in enumerate(s):  
        
    if i< mid:
        first+=ch
    elif i==mid and len(s)%2==0:    
        middle+=ch        
    else:
        second+=ch   
print("First Half :", first)
print("Middle:",middle)
print("Second Half :", second)  
#48
s = input("Enter a string: ")
mid = len(s) // 2
first = ""
middle=""
second = ""
for i, ch in enumerate(s):  
        
    if i< mid:
        first+=ch        
    else:
        second+=ch   
if first==second:
    print("Equal Halves")
else:      
    print("Different Halves") 
#49 
s = input("Enter a string: ")
n = len(s)

symmetric = 0
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        symmetric=0
    else:
        symmetric+=1

if symmetric==0:
    print(" Not Symmetric")
else:
    print(" Symmetric") 
#50
s = input("Enter a string: ")
n = len(s)
for i in range(len(s)):
    if i%2==0:
        print(s[i]) 
#51 
s = input("Enter a string: ")
n = len(s)
even=0
odd=0
for i in range(len(s)):
    if i%2==0:
       even+=1
    else:
        odd+=1
print("even index:",even,"odd index:",odd) 
#52   
s = input("Enter a string: ")

result = ""
for i in range(0, len(s), 2):
    result += s[int(i) + 1] + s[i]
print(result) 
#53
import math

n = abs(int(input("Enter an integer: ")))
digits = int(math.log10(n)) + 1 
largest = -1
second = -1
for i in range(digits):
    d = n % 10
    if d > largest:
        second = largest
        largest = d
    elif d != largest and d > second:
        second = d
    n //= 10

if second == -1:
    print("No second largest digit")
else:
    print(second) 


                  
      



     




      
