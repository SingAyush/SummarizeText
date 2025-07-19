import uvicorn
import os
import sys
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from TextSummarizer.pipeline.prediction import PredictionPipeline


text:str = "Text Summarization is the process of shortening a set of data and creating a subset that represents the most important or relevant information within that data."

app = FastAPI()

@app.get("/",tags=[ "authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("train successfull")
    except Exception as e:
        return Response(f"train failed: {e}")
    
@app.get("/predict")
async def predict():
    try:
        pipeline = PredictionPipeline()
        summary = pipeline.run(text)
        return Response(f"Prediction successful: {summary}")
    except Exception as e:
        return Response(f"Prediction failed: {e}")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

