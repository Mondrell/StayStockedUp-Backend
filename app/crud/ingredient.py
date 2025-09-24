from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate

def create_ingredient(db: Session, ingredient: IngredientCreate):
    db_ingredient = Ingredient(name=ingredient.name, quantity=ingredient.quantity)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

def get_ingredients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ingredient).offset(skip).limit(limit).all()
