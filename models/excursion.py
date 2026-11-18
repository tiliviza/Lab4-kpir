from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Excursion(Base):
    __tablename__ = "excursions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True) 
    price = Column(Float) 
    duration_hours = Column(Integer) 
    guide_id = Column(Integer, ForeignKey("guides.id"))
    guide = relationship("Guide")