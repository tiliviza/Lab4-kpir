from sqlalchemy.orm import Session
from models.guide import Guide

class GuideRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, full_name: str, city: str, contact_phone: str):
        guide = Guide(full_name=full_name, city=city, contact_phone=contact_phone)
        self.session.add(guide)
        self.session.commit()
        self.session.refresh(guide)
        return guide

    def get_by_id(self, guide_id: int):
        return self.session.query(Guide).filter(Guide.id == guide_id).first()

    def get_all(self):
        return self.session.query(Guide).all()

    def update_city(self, guide_id: int, new_city: str):
        guide = self.get_by_id(guide_id)
        if guide:
            guide.city = new_city
            self.session.commit()
        return guide

    def delete(self, guide_id: int):
        guide = self.get_by_id(guide_id)
        if guide:
            self.session.delete(guide)
            self.session.commit()