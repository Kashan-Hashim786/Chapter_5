# Dictionary is a collection of key value pairs
Bank_Loan_Defaulters = {}   # emplty dictionary
Bank_Loan_Defaulters = {
  "Ahamd Raza" : 12500,
  "Saud Ahmad" : 76000,
  "Noor Ilahi" : 10000,
  "Sanam Dilshad" : 12300,
  "Nusrat Butt" : 35000,
  "Agha Kaleem" : 65000,
   12500 : "Naseem Shah",
   "Saud Ahmad" : 76540
}
'''
 It is unordered. 
 It is mutable. 
 It is indexed. 
 Cannot contain duplicate keys.
'''
Bank_Loan_Defaulters["Noor Ilahi"] = 9000
# print(Bank_Loan_Defaulters[0])   # not allowed in python
print(Bank_Loan_Defaulters["Noor Ilahi"])
print(Bank_Loan_Defaulters["Sanam Dilshad"])
print(Bank_Loan_Defaulters["Ahamd Raza"])
print(Bank_Loan_Defaulters["Saud Ahmad"])
print(Bank_Loan_Defaulters[12500])
#print(Bank_Loan_Defaulters["Saud Ahmad"])  

