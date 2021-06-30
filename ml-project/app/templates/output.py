

from pydantic import BaseModel


class OutputTemplate(BaseModel):
    categ:float
    categ_prob:float
