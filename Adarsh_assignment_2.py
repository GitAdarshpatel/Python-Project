print("Q.1.Ans")
str='Python is a case sensitive language'
#(a)
print( len(str))
#(b)asd
print( str[::-1])
#(c)
s1=str[10:26]
print( s1)
#(d)
s2=str[0:10],str[27:]
print(s2)
#(e)
indx=str.find("a")
print( indx)
#(f)
s3=str.replace(' ', '')
print('\n(f)input string with white spaces removed:\n', s3)

#Ques.2
print('Q.2.ans.')
Name=input('Enter your name:\n')
SID=int(input('\nEnter your SID:\n'))
Dep_name=input('\nEnter your Department name:\n')
CGPA=float(input('\nEnter your CGPA:\n'))
print('Hey, {s} Here!'.format(s=Name))
print('My SID is {d}'.format(d=SID))
print('I am from {s} department and my CGPA is {f}'.format(s=Dep_name,f=CGPA))

#QUES3
print("Q.3.ans")
a=56
b=10
#(a)
print('\n(a)  a&b =', a&b)
#(b)
print('\n(b) a|b =', a|b)
#(c)
print('\n(c) a^b =', a^b)
#(d)
print('\n(d)')
print('After left shift by 2-bits, a =', a<<2)
print('After left shift by 2-bits, b =', b<<2)
#(e)
print('\n(e)')
print('After right shift by 2-bits, a=', a>>2)
print('After right shift by 4-bits, b=',b>>4)

#QUES4
print ('Ans 4')
def isWordPresent(sentence, word):
    s = sentence.split(" ")
    for i in s:
        if (i == word):
            return True
    return False
B = input('Enter the sentence/string -\n')
word ='name'
if word in B:
    print('\nYes')
else:
    print('\nNo')

#QUES5
print('Ans 5')
L1 = int(input('\nEnter the 1st length:\n'))
L2 = int(input('\nEnter the 2nd length:\n'))
L3 = int(input('\nEnter the 3rd length:\n'))
if L1>(L2+L3) or L2>(L1+L2) or L3>(L1+L2):
    print('\n No,entered three lengths can not form a triangle')
else:
    print('\n Yes,entered three lengths can form a triangle')

#QUES6
print('Ans6')
def countFlips(a, b):
    flips = 0
    while(a > 0 or b > 0):
      t1 = (a & 1)
      t2 = (b & 1)                                     
      if(t1 != t2):
            flips += 1
      a>>=1
      b>>=1
    return flips
a = int(input('enter value of a:\n'))
b = int(input('enter value of b:\n'))
print(countFlips(a, b))
 

    









