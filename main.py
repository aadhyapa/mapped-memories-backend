from fastapi import FastAPI
import os
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv()

app = FastAPI()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


# To run the application, use the command:
# uvicorn main:app --reload