from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] =  os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "fastapi_tutorial"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

#create a llm chain
promptTemplate = ChatPromptTemplate.from_template("Explain {concept} to me as you would do for a {audience} within 50 words")

model = ChatGroq(model="mixtral-8x7b-32768")

parser = StrOutputParser()

chain = promptTemplate|model|parser


app = FastAPI(
    title="Exposit",
    version="1.0",
    description="A simple API server to a Basic Langchain application for exposition",
)

add_routes(
    app=app,
    runnable=chain,
    path="/exposition"
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8080)