from sqlalchemy.orm import Session
from app import models, schemas

def get_ingredients(db: Session):
    return db.query(models.Ingredient).all()

def create_ingredient(db: Session, ingredient: schemas.IngredientCreate):
    db_obj = models.Ingredient(**ingredient.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

