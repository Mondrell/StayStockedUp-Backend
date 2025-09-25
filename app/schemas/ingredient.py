from pydantic import BaseModel

# Shared props
class IngredientBase(BaseModel):
    name: str
    quantity: int

# Body for POST/creation
class IngredientCreate(IngredientBase):
    pass

# Response model (has id)
class Ingredient(IngredientBase):
    id: int

    class Config:
        # replaces orm_mode=True in Pydantic v2
        from_attributes = True
