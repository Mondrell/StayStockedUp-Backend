from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.schemas.ingredient import Ingredient, IngredientCreate, IngredientUpdate
from app.crud.ingredient import (
    get_ingredients,
    get_ingredient_by_id,
    create_ingredient as create_ingredient_crud,
    update_ingredient as update_ingredient_crud,
    delete_ingredient as delete_ingredient_crud,
)

router = APIRouter(prefix="/ingredients", tags=["ingredients"])

@router.get("/", response_model=List[Ingredient])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_ingredients(db, skip=skip, limit=limit)

@router.get("/{ingredient_id}", response_model=Ingredient)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    item = get_ingredient_by_id(db, ingredient_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return item

@router.post("/", response_model=Ingredient)
def create_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    return create_ingredient_crud(db=db, ingredient=ingredient)

@router.put("/{ingredient_id}", response_model=Ingredient)
def update_ingredient(ingredient_id: int, ingredient: IngredientUpdate, db: Session = Depends(get_db)):
    item = update_ingredient_crud(db, ingredient_id, ingredient)
    if item is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return item

@router.delete("/{ingredient_id}", response_model=Ingredient)
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    item = delete_ingredient_crud(db, ingredient_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return item
