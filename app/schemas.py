from pydantic import BaseModel

class DeviceBase(BaseModel):
    product_name: str
    device_group_name: str
    description: str

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: str

    class Config:
        orm_mode = True
