import lstm_crf.function

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chineseNER/{item_str}")
def read_item(item_str: str):
    ner = NER("predict")
    print(ner.predict(item_str))
    return {"item_str": item_str}

def test_predict(item_str: str):
    ner = NER("predict")
    print(ner.predit(item_str))
    