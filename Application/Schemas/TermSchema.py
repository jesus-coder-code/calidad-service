from pydantic import BaseModel
from typing import Optional, List

from Application.Schemas.ActionPlanSchema import ActionPlanSchemaResponse


class TermRequest(BaseModel):
    vigencia: int

    class Config:
        from_attributes = True


class TermBaseResponse(BaseModel):
    id: Optional[int]
    vigencia: int

    class Config:
        from_attributes = True


class TermResponse(BaseModel):
    id: Optional[int]
    vigencia: int
    planes: List[ActionPlanSchemaResponse] = []

    class Config:
        from_attributes = True
