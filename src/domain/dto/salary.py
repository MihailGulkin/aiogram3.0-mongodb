import datetime

from pydantic import BaseModel


class Salary(BaseModel):
    dataset: list[int]
    labels: list[datetime.datetime]
