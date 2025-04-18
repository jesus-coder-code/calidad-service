import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Infrastructure.DB.Database import create_db_and_tables
from WebApi.Controllers import (
    ActionPlanController,
    AuthController,
    ActivitiesController,
    ComponentsController,
)
import uvicorn

# app = FastAPI(title="Calidad service")

# Registra las rutas de autenticación
# app.include_router(api_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthController.router, prefix="/api", tags=["Login"])
app.include_router(ActivitiesController.router, prefix="/api", tags=["Activities"])
app.include_router(ActionPlanController.router, prefix="/api", tags=["Action Plans"])
app.include_router(ComponentsController.router, prefix="/api", tags=["Components"])

# Punto de entrada de la aplicación
if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)
