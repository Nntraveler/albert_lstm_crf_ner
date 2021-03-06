import function

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chineseNER/{item_str}")
def read_item(item_str: str):
    ner = function.NER("predict")
    entities = ner.predict(item_str)
    return entities

def test_predict(item_str: str):
    ner = function.NER("predict")
    print(ner.predict(item_str))
    
