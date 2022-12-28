from fastapi import APIRouter, Body
from models.clt import CLTBase
from models.pj import PJBase
from models.schemas.compare import CompareInputSchema
from services.compare import compare_clt_pj, compare_pj_clt

router = APIRouter()


@router.post('/clt')
def get_compare_clt_pj(input: CompareInputSchema = Body(...)):
    clt = CLTBase(**input.dict())
    return compare_clt_pj(clt, input.attachment)


@router.post('/pj')
def get_compare_pj_clt(input: PJBase = Body(...)):
    return compare_pj_clt(input)
