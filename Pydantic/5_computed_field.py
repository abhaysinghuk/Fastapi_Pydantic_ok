from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

#Step_1 (pydantic model made)
class Patient(BaseModel):

    #type validation also we have done data validation

    name: str
    email: EmailStr
    age:  int
    height: float
    weight: float
    married: bool = False # defalt value as False
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float: #output will be float of this 
    
        bmi = round(self.weight/(self.height**2),2)

        return bmi

    


#Step_2 (now creating the pydantic object)

patient_info = {'name': 'Abhay', 'age': 70, 'email': 'yes@gmail.com', 'weight': 78.9, 'height': 1.72, 'Linkedin': 'http://linkedin.com/abhaysinghuk', 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': { 'mobile_number': '9232133245', 'emergency':'8865976249'}} #dicnory

patient1 = Patient(**patient_info) #made a object patient1 of Patient class and passed a dicnory in this

# Step_3

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('BMI', patient.calculate_bmi)
    
    print('inserted')


#calling 

insert_patient_data(patient1)




