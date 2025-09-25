from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient as IngredientModel
from app.schemas.ingredient import IngredientCreate, IngredientUpdate

def get_ingredients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(IngredientModel).offset(skip).limit(limit).all()

def get_ingredient_by_id(db: Session, ingredient_id: int):
    return db.query(IngredientModel).filter(IngredientModel.id == ingredient_id).first()

def create_ingredient(db: Session, ingredient: IngredientCreate):
    obj = IngredientModel(**ingredient.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_ingredient(db: Session, ingredient_id: int, ingredient: IngredientUpdate):
    obj = db.query(IngredientModel).filter(IngredientModel.id == ingredient_id).first()
    if not obj:
        return None
    for k, v in ingredient.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def delete_ingredient(db: Session, ingredient_id: int):
    obj = db.query(IngredientModel).filter(IngredientModel.id == ingredient_id).first()
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
