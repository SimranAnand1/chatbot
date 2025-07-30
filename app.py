# module import
import qa 
import nextword

# fastapi imports
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import base64

# generating objects
object_qa=qa.ques_ans()
object_nw=nextword.next_word()

# starting ap
app=FastAPI()

# app test
@app.get("/")
async def main():
    return {'TEST': 'Pass'}

@app.post("/text/")
async def text_message(text: str):
    json_compatible_item_data = jsonable_encoder(text)
    return JSONResponse(content=json_compatible_item_data)

########## Post requests ##########
class Text(BaseModel):
    content: str

@app.post("/Question_Answering")
async def post_item(text: Text):
    result=object_qa.gen_qa(text.content)
    return {"Answer is": result}

@app.post("/Generate and predict Next Word")
async def post_item(text: Text):
    res=object_nw.gen_word(text.content)
    return {"The Predicted Text is" : res}

