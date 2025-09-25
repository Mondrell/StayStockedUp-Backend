# app/schemas/ingredient.py
from pydantic import BaseModel
from typing import Optional


class IngredientBase(BaseModel):
    name: str
    current_inventory: int
    restock_threshold: int
    inventory_status: str
    category: Optional[str] = None
    user: Optional[str] = None
    restaurant_name: Optional[str] = None


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    current_inventory: Optional[int] = None
    restock_threshold: Optional[int] = None
    inventory_status: Optional[str] = None
    category: Optional[str] = None
    user: Optional[str] = None
    restaurant_name: Optional[str] = None


class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True
