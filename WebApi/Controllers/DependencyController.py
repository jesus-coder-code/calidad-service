from fastapi import APIRouter, Depends, HTTPException, status
from Application.UseCases.DependencyUseCases.GetDependenciesUseCase import (
    GetDependenciesUseCase,
)
from Application.UseCases.DependencyUseCases.GetDependencyByIdUseCase import (
    GetDependencyByIdUseCase,
)
from Application.UseCases.DependencyUseCases.CreateDependencyUseCase import (
    CreateDependencyUseCase,
)
from Application.UseCases.DependencyUseCases.UpdateDependencyUseCase import (
    UpdateDependencyUseCase,
)
from Application.UseCases.DependencyUseCases.DeleteDependencyUseCase import (
    DeleteDependencyUseCase,
)
from Infrastructure.Repositories.DependencyRepository import DependencyRepository
from Domain.Entities.Dependencies import Dependencies
from Application.Schemas.DependencySchema import *
from Infrastructure.utils.verifyApiKey import verify_api_key


router = APIRouter()


@router.get("/dependency/GetDependencies", dependencies=[Depends(verify_api_key)])
async def get_dependencies():
    dependencyRepository = DependencyRepository()
    use_case = GetDependenciesUseCase(dependencyRepository)
    dependencies = await use_case.execute()
    data = [
        DependencyResponse.model_validate(dependency) for dependency in dependencies
    ]
    return {"message": "success", "data": data, "status": 200}


@router.post(
    "/dependency/CreateDependency",
    dependencies=[Depends(verify_api_key)],
    response_model=DependencyBaseResponse,
)
async def create_dependency(dependency: DependencyRequest):
    dependency_model = Dependencies(**dependency.model_dump())
    dependencyRepository = DependencyRepository()
    use_case = CreateDependencyUseCase(dependencyRepository)
    created_plan = await use_case.execute(dependency_model)
    return created_plan


@router.put(
    "/dependency/UpdateDependency/{dependency_id}",
    dependencies=[Depends(verify_api_key)],
)
async def update_dependency(dependency_id: int, dependency: DependencyRequest):
    dependency_model = Dependencies(**dependency.model_dump())
    dependencyRepository = DependencyRepository()
    use_case = UpdateDependencyUseCase(dependencyRepository)
    update_dependency = await use_case.execute(dependency_id, dependency_model)

    if update_dependency is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="esta dependencia para actualizar no existe",
        )

    return {"message": "dependencia actualizada correctamente"}


@router.delete(
    "/dependency/DeleteDependency/{dependency_id}",
    dependencies=[Depends(verify_api_key)],
)
async def delete_dependency(dependency_id: int):
    dependencyRepository = DependencyRepository()
    use_case = DeleteDependencyUseCase(dependencyRepository)
    success = await use_case.execute(dependency_id)

    if success is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="dependencia no encontrada"
        )

    return {"message": "dependencia eliminada correctamente correctamente"}


@router.get(
    "/dependency/GetDependencyById/{dependency_id}",
    dependencies=[Depends(verify_api_key)],
)
async def get_dependendcy_by_id(dependency_id: int):
    dependencyRepository = DependencyRepository()
    use_case = GetDependencyByIdUseCase(dependencyRepository)
    dependency = await use_case.execute(dependency_id)

    if dependency is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="esta dependencia no existe no existe",
        )

    data = DependencyResponse.model_validate(dependency)
    return {"message": "success", "data": data, "status": 200}
