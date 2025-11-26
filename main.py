import uvicorn
from api import routs
if __name__ == '__main__':
    uvicorn.run("main:routs.app", host="localhost",port=8000 , reload=True)