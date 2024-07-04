from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import models, schemas, database

models.Base.metadata.create_all(database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/device")
async def read_device(db: Session = Depends(get_db)):
    db_item = db.query(models.Device).all()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_item

@app.post("/api/v1/device", response_model=schemas.Device)
async def create_device(item: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db_item = models.Device(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/api/v1/device/{device_id}", response_model=schemas.Device)
async def update_device(device_id: str, item: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Device).filter(models.Device.id == device_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Device not found")
    for key, value in item.dict().api/v1/device():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/api/v1/device/{device_id}", response_model=schemas.Device)
async def delete_device(device_id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.Device).filter(models.Device.id == device_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item

# if __name__ == "__main__":
# 	import uvicorn
# 	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)