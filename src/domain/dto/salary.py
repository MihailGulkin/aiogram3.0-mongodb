from pydantic import BaseModel


class Salary(BaseModel):
    dataset: list[int]
    labels: list[str]
