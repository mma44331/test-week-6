from classes.clasess import Soldier
from fastapi import UploadFile, FastAPI
import csv
import io


def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}
    # Read file bytes
    content = file.file.read().decode("utf-8")
    # Parse CSV
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    soldier = []
    for item in rows:
        personal_number, first_name, last_name, gender, city, distance = item
        sold = Soldier(personal_number, first_name, last_name, gender, city, distance,"man")
        soldier.append(sold)
    soldier.sort(key=lambda soldier: soldier.distance)


    return  rows