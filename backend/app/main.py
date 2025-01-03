from fastapi import FastAPI
from app.routers import auth, chat, group, channel, notifications

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(group.router, prefix="/group", tags=["Group"])
app.include_router(channel.router, prefix="/channel", tags=["Channel"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

@app.get("/")
async def root():
    return {"message": "Welcome to the MeetMe API"}