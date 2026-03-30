from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat import router as chat_router
# import uvicorn

app = FastAPI()

# Enabling CORS so the C# backend and frontend can talk to the AI_Sevice
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#
app.include_router(chat_router, tags=["Chatbot"])

@app.get("/")
async def root():
    return {"m/essage": "Good day, how have you been today?"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)