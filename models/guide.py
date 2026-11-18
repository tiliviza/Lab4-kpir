from sqlalchemy import Column, Integer, String
from database import Base

class Guide(Base):
    __tablename__ = "guides"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    city = Column(String)  
    contact_phone = Column(String)