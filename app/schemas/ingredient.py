from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    current_inventory: int
    restock_threshold: int
    inventory_status: str
    category: str
    user: str
    restaurant_name: str

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        from_attributes = True  # ✅ tells Pydantic to read from SQLAlchemy objects
