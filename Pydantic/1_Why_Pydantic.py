def intert_info_patiant(name, age):

    if type(name) == str and type(age) == int: #doing typevalidation
        if age < 0: # doing data validation
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError('Incorrect datatype')
     

def update_patient_data(name, age):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError('Incorrect datatype')



intert_info_patiant('abhi', 2)