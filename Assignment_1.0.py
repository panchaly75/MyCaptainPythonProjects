#Question: Can we update the value of a key in dictionary? if yes, then how?
'''
yes, we update a value of a key in dictionary by following
'''

dict0 = {"Y" : "yttrium", "As" : "arsenic"}
dict0["H"] = "helium"                                                           #line 7 : explain how to new key-value pair make
for key in dict0:
    print(key,"=",dict0[key])

print("\n")

dict0["H"] = "hydrogen"                                                         #line 13 : explain how to update key-value pair
for key in dict0:
    print(key,"=",dict0[key])
