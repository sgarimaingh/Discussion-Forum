from fastapi import FastAPI
import uvicorn
from user_service.controller import user_router
from discussion_service.controller import discussion_router
from interaction_service.controller import interaction_router
from config.database import db
from user_service.models import User, Follow
from discussion_service.models import Discussion
from interaction_service.models import Comment, Like, View

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(discussion_router, prefix="/discussions", tags=["discussions"])
app.include_router(interaction_router, prefix="/interactions", tags=["interactions"])

@app.on_event("startup")
def on_startup():
    # Connect to the database and create tables
    db.connect()
    db.create_tables([User, Follow, Discussion, Comment, Like, View], safe=True)

@app.on_event("shutdown")
def on_shutdown():
    if not db.is_closed():
        db.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
