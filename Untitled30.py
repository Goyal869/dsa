#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
l=[int(x) for x in input("Enter numbers").split()]
sum=int(input("sum"))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==sum:
            print("pair of two integers present at",[i,j],"will be",sum )


# In[2]:


#Write a program to reverse an array in place?
#In place means you cannot create a new array. You have to update the original array.


def reverse(array):
    start=0
    end= len(array)-1
    for m in range(0,len(array)//2):
        array[start],array[end]=array[end],array[start]
        start=start+1
        end=end-1
    return array

array=[int(x) for x in input().split()]
reverse(array)


# In[16]:


#Write a program to check if two strings are a rotation of each other?
string=input("enter string")
string1=input("enter string")
if string[::-1]==string1:
    print("They are rotation")
else:
    print("False")


# In[6]:


# Write a program to print the first non-repeated character from a string?
myStr = "Shuhubh"
while myStr != "":
    string_len0 = len(myStr)
    ch = myStr[0]
    myStr = myStr.replace(ch, "")
    string_len1 = len(myStr)
    if string_len1 == string_len0-1:
        print ("First non-repeating character = ",ch)
        break
else:
    print ("No Unique Character Found!")
    


# In[29]:


#Write a program to find the smallest number using a stack.
class stack:
    def __init__(self):
        self.array=[]
    def push(self,item):
        self.array.append(item)
        return item
    def pop(self):
        if len(self.array)==0:
            return "stack empty"
        return self.array.pop()
    def peek(self):
        return self.array[-1]
x=stack()
print(x.push(10))
print(x.push(20))
print(x.pop())
print(x.pop())
print(x.pop())

    


# In[ ]:





# In[3]:


#tower of hanoi 
def TowerOfHanoi(n , s_pole, d_pole, i_pole):           
    if n == 1:
        print("Move disc 1 from pole",s_pole,"to pole",d_pole)
        return
    TowerOfHanoi(n-1, s_pole, i_pole, d_pole)
    print("Move disc",n,"from pole",s_pole,"to pole",d_pole)
    TowerOfHanoi(n-1, i_pole, d_pole, s_pole)
n=3
TowerOfHanoi(n, 'A', 'B', 'C')


# In[33]:


#Write a program to reverse a stack
class stack:
    def __init__(self):
        self.array=[]
        self.array2=[]
    def push(self,item):
        
        self.array.append(item)
        return self.array
       
    def reverse_stack(self):
        if len(self.array)==0:
            print("empty")
            return
        
        for i in range(len(self.array)):
            x=self.array.pop()
            self.array2.append(x)
        print(self.array2)
x=stack()
n=int(input("no. of ele in stack"))
i=0
while i<n:
    item=int(input())
    x.push(item)
    i+=1

x.reverse_stack()
    



# In[14]:


# Write a program to check if all the brackets are closed in a given code snippet.
string="([{}])"
stack=[]
for i in range(len(string)):
    if (string[i]=="[" or string[i]=="{" or string[i]=="("):
        stack.append(string[i])
    elif (len(stack)!=0 and stack[-1]=="{" and string[i]=="}"):
        stack.pop()
    elif (len(stack)!=0 and stack[-1]=="[" and string[i]=="]"):
        stack.pop()
    elif (len(stack)!=0 and stack[-1]=="(" and string[i]==")"):
        stack.pop()
    else:
        print("false")
if len(stack)==0:
    print(True)
else:
    print(False)


# In[3]:


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
# solution:
def isOperator(x):
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "/":
        return True
    if x == "*":
        return True
    return False
def postToPre(post_exp):
    s = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
 
    ans = ""
    for i in s:
        ans += i
    return ans
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))


# In[4]:


# Q7. Write a program to convert prefix expression to infix expression.
# solution:
def prefixToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
    
str = "*-A/BC-/AKL"
print("infix is:",prefixToInfix(str))


# In[5]:


# Q10. Write a program to find the smallest number using a stack.
# solution:     
arr = [25, 91, 44, 75, 16]
x = arr[0]      
for i in range(0, len(arr)):  
    if(arr[i] < x):    
        x = arr[i];    
print("Smallest element present in given array is",x)


# In[ ]:




