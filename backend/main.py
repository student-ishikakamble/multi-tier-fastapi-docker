from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from backend.database import SessionLocal, engine, Base
from backend import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- CREATE ----------------
@app.post("/user")
def create_user(name: str, db: Session = Depends(get_db)):
    user = models.User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# ---------------- READ ----------------
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# ---------------- UPDATE ----------------
@app.put("/user/{user_id}")
def update_user(user_id: int, name: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = name
    db.commit()
    db.refresh(user)

    return {"message": "User updated successfully", "user": user}


# ---------------- DELETE ----------------
@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}
    import os
import uvicorn

port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
    @app.get("/")
def home():
    return {"message": "FastAPI is running successfully 🚀"}