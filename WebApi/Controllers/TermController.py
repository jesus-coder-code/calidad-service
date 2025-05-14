from fastapi import APIRouter, HTTPException, status
from Infrastructure.Repositories.TermRepository import TermRepository
from Domain.Entities.Term import Term
from Application.UseCases.TermUseCases.GetAllTermsUseCase import GetAllTermsUseCase
from Application.UseCases.TermUseCases.CreateTermUseCase import CreateTermUseCase
from Application.UseCases.TermUseCases.UpdateTermUseCase import UpdateTermUseCase
from Application.UseCases.TermUseCases.DeleteTermUseCase import DeleteTermUseCase
from Application.UseCases.TermUseCases.GetTermByIdUseCase import GetTermByIdUseCase
from Application.Schemas.TermSchema import *

router = APIRouter()


@router.get("/term/GetTerm")
async def get_term():
    use_case = GetAllTermsUseCase(TermRepository())
    terms = await use_case.execute()
    data = [TermBaseResponse.model_validate(term) for term in terms]
    return {"message": "success", "data": data, "status": 200}


@router.post("/term/CreateTerm", response_model=TermBaseResponse)
async def create_term(term: TermRequest):
    term_model = Term(**term.model_dump())
    use_case = CreateTermUseCase(TermRepository())
    created_term = await use_case.execute(term_model)

    if created_term is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="esta vigencia ya existe"
        )
    return created_term
