import uvicorn
from fastapi import UploadFile, FastAPI
from data.uplode_csv import upload_csv
from data.tablse import *

app = FastAPI()
@app.get("/get-")
@app.post("/assignWithCsv")
def uplode_csv_to_db(file: UploadFile):
    file_csv = upload_csv(file)
    insert_soldier_to_table(file_csv)
    return upload_csv(file)

@app.post("/insert-soldier")
def insert_soldier():
    pass
