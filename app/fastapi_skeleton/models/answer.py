
# from typing import List
from pydantic import BaseModel


class AnswerTranscription(BaseModel):
    answer:str


# def review_to_list(score: ReviewTexts) -> List:
#     return [
#         score.review]
