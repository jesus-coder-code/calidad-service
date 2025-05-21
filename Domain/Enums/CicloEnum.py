from enum import Enum


class CicloEnum(str, Enum):
    PLANEAR = "planear"
    HACER = "hacer"
    VERIFICAR = "verificar"
    ACTUAR = "actuar"
