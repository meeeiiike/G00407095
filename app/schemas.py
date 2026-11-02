from typing import Annotated

from pydantic import BaseModel

BorrowerNameStr = Annotated[str, StringConstraints(min_length = 2, max_length = 60)]
PurposeStr = Annotated[str, StringConstraints(min_length = 5, max_length = 100)]

class LoanCreate(BaseModel):
    borrower_name: BorrowerNameStr
    equipment_id: int=Field(gt=0)
    loan_days: int=Field(gt=0, lt=15)
    purpose: PurposeStr
    #status: 
