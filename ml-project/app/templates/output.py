

from pydantic import BaseModel


class OutputTemplate(BaseModel):
    categ:str
    categ_prob:float
