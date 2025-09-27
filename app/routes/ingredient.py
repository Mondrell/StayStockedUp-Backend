from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db import get_db

router = APIRouter()

@router.get("/ingredients/", response_model=list[schemas.Ingredient])
def get_all_ingredients(db: Session = Depends(get_db)):
    return crud.ingredient.get_ingredients(db)

@router.post("/ingredients/", response_model=schemas.Ingredient)
def create_ingredient(ingredient: schemas.IngredientCreate, db: Session = Depends(get_db)):
    return crud.ingredient.create_ingredient(db, ingredient)


