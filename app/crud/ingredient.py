from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient as IngredientModel
from app.schemas.ingredient import IngredientCreate

def create_ingredient(db: Session, item: IngredientCreate):
    db_item = IngredientModel(name=item.name, quantity=item.quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_ingredients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(IngredientModel).offset(skip).limit(limit).all()
