from models.clt import CLT, CLTBase
from models.pj import PJ, AttachmentEnum
from pydantic import BaseModel


class CompareInputSchema(CLTBase):
    attachment: AttachmentEnum


class CompareResponseSchema(BaseModel):
    clt: CLT
    pj: PJ
