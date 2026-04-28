from fastapi import FastAPI, Path, Query, HTTPException
import json 

app = FastAPI()

# making a function to load the data of that json file

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    
    return data


@app.get("/")
def hello():
    return {'message': 'Patient management system API'}

@app.get("/about")
def about():
    return {"message":"A fully functional API to manage the patient history"}

# creating a new end point which give all the patient data

@app.get('/view')
def view():
    # getting the data 
    data = load_data()

    return data

## defining my route

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of a patient is the DB', example = 'P001')):
    ## pehele hum sara data load karege then search karege ki ye specific id hai.
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort') #... means it is requied not optional
def sort_patient(sort_by: str = Query(..., description = 'sort on the basic of weight, height or bmi'), order: str = Query('asc', description='sort in asc or desc' )):
    valid_field = ['height', 'weight', 'bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f'invalid field select from {valid_field}')
    
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=404, detail='Invalid order is selected b/w asc and desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

