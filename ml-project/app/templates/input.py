# from typing import List
from typing import Optional
from pydantic import BaseModel


class InputTemplate(BaseModel):
    id_survey_response: Optional[str] = "0a0a0a"
    campaign: Optional[str] = "1b1b1b1"
    campaign_name: Optional[str] = "sin_campaña"
    answer:str