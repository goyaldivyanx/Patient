from fastapi import FastAPI,Path,HTTPException,Query
import json
from pydantic import BaseModel,computed_field
import os

app = FastAPI()




#function to laod data from json
def load_all_data():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'PatientData.json')
    with open(json_path, 'r') as f1:
        data = json.load(f1)
    return data
        

#Endpoint 1 : Home Page
@app.get("/")
def Welcome():
    return({'message': 'Welcome to Patient Management System API'})



#Endpoint 2: About Us Page
@app.get("/about")
def  About():
    return({'message': 'This is a fully functional API module for a Pateint management System providing various functionality of CRUDD operations'})



#Endpoint 3 : Provide the data all off the pateints 
@app.get("/allpatient")
def displayall():
    data = load_all_data()
    return data
 
 
 
 #EndPoint 4 : Searching Patient
@app.get("/patient/{p_id}")
def display(p_id:str = Path(...,title="Patient ID",example="Pxxx")):
     data = load_all_data()
     if p_id in data:
         return data[p_id]
     raise HTTPException(404,"Patient Not Found")
 
 
 
 #EndPoint 5 : Sorting Data
@app.get("/sorted_data")
def sort(sort_by: str=Query(),order :str = Query()):
    vf = ['height','Weight','bmi']
    if sort_by not in vf:
        raise HTTPException(400,f'Invalid Feild, Select from {vf}')
    vf2 = ['asc','desc']
    if order not in vf2:
        raise HTTPException(400,f'Invalid Feild, Select from {vf2}')
    
    data=load_all_data()
    order=True if order=="desc" else False
    sort_data = sorted(data.values(),key=lambda x : x.get(sort_by,0),reverse=order)
    return sort_data
     