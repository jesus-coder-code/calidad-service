from fastapi import APIRouter, Depends, HTTPException, status
from Infrastructure.Repositories.PoliticsRepository import PoliticsRepository
from Application.UseCases.PoliticsUseCases.GetPoliticsUseCase import GetPoliticsUseCase
from Application.UseCases.PoliticsUseCases.CreatePoliticUseCase import (
    CreatePoliticUseCase,
)
from Application.UseCases.PoliticsUseCases.UpdatePoliticUseCase import (
    UpdatePoliticUseCase,
)
from Application.Schemas.PoliticSchema import (
    PoliticSchemaResponse,
    PoliticSchemaBaseResponse,
    PoliticSchemaRequest,
)

from Domain.Entities.Politics import Politics

router = APIRouter()


@router.get("/politics/GetPolitics")
async def get_politics():
    politicsRepository = PoliticsRepository()
    use_case = GetPoliticsUseCase(politicsRepository)
    politics = await use_case.execute()
    data = [PoliticSchemaResponse.model_validate(politic) for politic in politics]
    return {"message": "success", "data": data, "status": 200}


@router.post("/politics/CreatePolitic", response_model=PoliticSchemaBaseResponse)
async def create_politic(politic: PoliticSchemaRequest):
    politic_model = Politics(**politic.model_dump())
    politicsRepository = PoliticsRepository()
    use_case = CreatePoliticUseCase(politicsRepository)
    created_politic = await use_case.execute(politic_model)
    return created_politic


@router.put("/politics/UpdatePolitic/{politic_id}")
async def update_politic(politic_id: int, politic: PoliticSchemaRequest):
    politicsRepository = PoliticsRepository()
    politic_model = Politics(**politic.model_dump())
    use_case = UpdatePoliticUseCase(politicsRepository)
    update_politic = await use_case.execute(politic_id, politic_model)

    if update_politic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="esta politica no existe"
        )

    return {"message": "politica actualizada correctamente"}


"""@router.delete("/politics/DeletePolitic")
async def delete_politic():
    return {"message": "delete politic"}"""
