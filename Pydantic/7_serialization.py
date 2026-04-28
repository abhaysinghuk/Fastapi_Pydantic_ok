from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    country: str

class Patient(BaseModel):

    name: str
    age: int
    gender: str
    address: Address

address_dict = {'city': 'New York', 'state': 'NY', 'country': 'USA'}

address1 = Address(**address_dict)

patient_dict = {
    'name': 'John Doe',
    'age': 30,
    'gender': 'male',
    'address': address1
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.country)

## calling the patientic object model 

temp = patient1.model_dump_json()

print(temp)
print(type(temp))