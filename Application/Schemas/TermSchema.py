from pydantic import BaseModel
from typing import Optional, List

from Application.Schemas.ActionPlanSchema import ActionPlanSchemaResponse
from Domain.Enums.TermEnum import TermEnum


class TermRequest(BaseModel):
    vigencia: int
    estado: TermEnum

    class Config:
        from_attributes = True
        use_enum_values = True


class TermBaseResponse(BaseModel):
    id: Optional[int]
    vigencia: int
    estado: TermEnum

    class Config:
        from_attributes = True
        use_enum_values = True


class TermResponse(BaseModel):
    id: Optional[int]
    vigencia: int
    estado: TermEnum
    planes: List[ActionPlanSchemaResponse] = []

    class Config:
        from_attributes = True
        use_enum_values = True
