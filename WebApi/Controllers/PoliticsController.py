from fastapi import APIRouter, Depends, HTTPException, status
from Application.UseCases.PoliticsUseCases.GetPoliticByIdUseCase import (
    GetPoliticByIdUseCase,
)
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
from Infrastructure.utils.verifyApiKey import verify_api_key

router = APIRouter()


@router.get("/politics/GetPolitics", dependencies=[Depends(verify_api_key)])
async def get_politics():
    politicsRepository = PoliticsRepository()
    use_case = GetPoliticsUseCase(politicsRepository)
    politics = await use_case.execute()
    data = [PoliticSchemaResponse.model_validate(politic) for politic in politics]
    return {"message": "success", "data": data, "status": 200}


@router.post(
    "/politics/CreatePolitic",
    dependencies=[Depends(verify_api_key)],
    response_model=PoliticSchemaBaseResponse,
)
async def create_politic(politic: PoliticSchemaRequest):
    politic_model = Politics(**politic.model_dump())
    politicsRepository = PoliticsRepository()
    use_case = CreatePoliticUseCase(politicsRepository)
    created_politic = await use_case.execute(politic_model)
    return created_politic


@router.put(
    "/politics/UpdatePolitic/{politic_id}", dependencies=[Depends(verify_api_key)]
)
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


@router.get(
    "/politics/GetPoliticById/{politic_id}", dependencies=[Depends(verify_api_key)]
)
async def get_politics(politic_id: int):
    politicsRepository = PoliticsRepository()
    use_case = GetPoliticByIdUseCase(politicsRepository)
    politic = await use_case.execute(politic_id)

    if politic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="esta politica no existe"
        )

    data = PoliticSchemaResponse.model_validate(politic)
    return {"message": "success", "data": data, "status": 200}
