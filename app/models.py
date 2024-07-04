from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import ulid

Base = declarative_base()

class Device(Base):
    __tablename__ = "devices"
    id = Column(String, primary_key=True, index=True, default=lambda: str(ulid.new()))
    product_name = Column(String)
    device_group_name = Column(String)
    description = Column(String)
