from fastapi import APIRouter, Body
from models.clt import CLTBase
from models.schemas.compare import CompareInputSchema
from services.compare import compare_clt_pj

router = APIRouter()


@router.post('/')
def get_compare_clt_pj(input: CompareInputSchema = Body(...)):
    clt = CLTBase(**input.dict())
    return compare_clt_pj(clt, input.attachment)
