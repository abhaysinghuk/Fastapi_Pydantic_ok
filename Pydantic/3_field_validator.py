from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

#Step_1 (pydantic model made)
class Patient(BaseModel):

    #type validation also we have done data validation

    name: Annotated[str, Field(max_length=50, min_length=5, title='Name of the patient', description='Give the name of patient less then 50 charaters', examples=['Abhay', 'Paru', 'navneet'] )]
    email: EmailStr
    Linkedin: AnyUrl
    age:  int
    weight: Annotated[float, Field(gt=50, strict=True)]  # weigth should be greater then 0 and field will validate it.
    married: bool = False # defalt value as False
    allergies: Annotated[Optional[List[str]], Field(default= None,max_length=5)]  # we put defalt value as None
    contact_details: Dict[str, str]

    # adding field validator using decorators

    @field_validator('email')
    @classmethod
    def email_validation(cls, value):

        valid_domain = ['hdfc.com', 'pnb.com']
        domain_name = value.split('@')[-1]

        if domain_name  not in valid_domain:
            raise ValueError('not a valid domain name')
        
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def transform_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('age should be b/w 0 to 100')


#Step_2 (now creating the pydantic object)

patient_info = {'name': 'Abhay', 'age': '20', 'email': 'yes@hdfc.com', 'weight': 78.9, 'Linkedin': 'http://linkedin.com/abhaysinghuk', 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': { 'mobile_number': '9232133245'}} #dicnory

patient1 = Patient(**patient_info) #validation -> type coercion #made a object patient1 of Patient class and passed a dicnory in this

# Step_3

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print(patient.Linkedin)
    print('inserted')


#calling 

insert_patient_data(patient1)




