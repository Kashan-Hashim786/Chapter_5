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

print(Bank_Loan_Defaulters.items()) # list the items
print(Bank_Loan_Defaulters.keys())   # keys on Left Hand Side
Bank_Loan_Defaulters.update({"Agha Kaleem" : 7690, "Kashan Hashim" : 97000})
print(Bank_Loan_Defaulters)
print(Bank_Loan_Defaulters.get("Kashan Hashim"))  # NO key found in dictionary Print "None"
print(Bank_Loan_Defaulters["Kashan Hashim"])      # Print an error
print(Bank_Loan_Defaulters)
print(Bank_Loan_Defaulters.popitem())
print(Bank_Loan_Defaulters.pop("Saud Ahmad"))
