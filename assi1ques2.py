#Ques 2
Gross_income=int(input("Enter your income $ :"))
noofdependents=int(input("enter no of dependents"))
Standard_deduction= 10000
additional_deduction=3000
total= Gross_income-Standard_deduction-(additional_deduction*noofdependents)
Tax_rate=20
Tax= (total*Tax_rate)/100
print(Tax)
