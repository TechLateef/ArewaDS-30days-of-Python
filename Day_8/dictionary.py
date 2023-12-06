empt_dct = {}

dog_dct ={"name":"Chally", "color":"brown","breed":"german","legs":"4","age":6}

student_dct = { "first_name":"Mubarak", "last_name":"Abdullateef", "gender":"M", "age":12, "marital":"single", "status":"Available", "skills":['python','Golan'], "country":"Nigeria", "city" :"Abuja", "address":{
        'street':'Space street',
        'zipcode':'02210'
    }}

print("Student dictionary lenght is: ", len(student_dct))
print("Value of skills: {} and datatype: {} ".format( student_dct['skills'], type(student_dct['skills'])))

student_dct["skills"].append(["HTML","Reactjs"])
print("Value of skills: {} and datatype: {} ".format( student_dct['skills'], type(student_dct['skills'])))

print('student dictionary keys are: ', student_dct.keys())

print('student dictionary values are: ', student_dct.values())

print('Changing the dictionary to a list of tuples using items() method: ', student_dct.items())

# Removing one 
student_dct.popitem()

del empt_dct