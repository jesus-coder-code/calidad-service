from fastapi import APIRouter, Depends, HTTPException, status
from Infrastructure.Repositories.TermRepository import TermRepository
from Domain.Entities.Term import Term
from Application.UseCases.TermUseCases.GetAllTermsUseCase import GetAllTermsUseCase
from Application.UseCases.TermUseCases.CreateTermUseCase import CreateTermUseCase
from Application.UseCases.TermUseCases.UpdateTermUseCase import UpdateTermUseCase
from Application.UseCases.TermUseCases.DeleteTermUseCase import DeleteTermUseCase
from Application.UseCases.TermUseCases.GetTermByYearUseCase import GetTermByYearUseCase
from Application.Schemas.TermSchema import *
from Infrastructure.utils.verifyApiKey import verify_api_key

router = APIRouter()


@router.get("/term/GetTerm", dependencies=[Depends(verify_api_key)])
async def get_term():
    use_case = GetAllTermsUseCase(TermRepository())
    terms = await use_case.execute()
    data = [TermResponse.model_validate(term) for term in terms]
    return {"message": "success", "data": data, "status": 200}


@router.post(
    "/term/CreateTerm",
    dependencies=[Depends(verify_api_key)],
    response_model=TermBaseResponse,
)
async def create_term(term: TermRequest):
    term_model = Term(**term.model_dump())
    use_case = CreateTermUseCase(TermRepository())
    created_term = await use_case.execute(term_model)

    if created_term is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="esta vigencia ya existe"
        )
    return created_term


@router.put("/term/UpdateTerm/{term_id}", dependencies=[Depends(verify_api_key)])
async def update_term(term_id: int, term: TermRequest):
    term_model = Term(**term.model_dump())
    use_case = UpdateTermUseCase(TermRepository())
    updated_term = await use_case.execute(term_id, term_model)

    if updated_term is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="esta vigencia no existe"
        )

    return {"message": "vigencia actualizada correctamente"}


@router.delete("/term/DeleteTerm/{term_id}", dependencies=[Depends(verify_api_key)])
async def delete_term(term_id: int):
    use_case = DeleteTermUseCase(TermRepository())
    success = await use_case.execute(term_id)

    if success is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="esta vigencia no existe"
        )

    return {"message": "vigencia eliminada correctamente"}


@router.get("/term/GetTermByYear/{term_year}", dependencies=[Depends(verify_api_key)])
async def get_term_by_year(term_year: int):
    use_case = GetTermByYearUseCase(TermRepository())
    term = await use_case.execute(term_year)

    if term is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="vigencia no encontrada"
        )

    data = TermResponse.model_validate(term)
    return {"message": "sucess", "data": data, "status": 200}
