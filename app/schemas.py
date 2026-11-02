from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

BorrowerNameStr = Annotated[str, StringConstraints(min_length = 2, max_length = 60)]
PurposeStr = Annotated[str, StringConstraints(min_length = 5, max_length = 100)]

class LoanCreate(BaseModel):
    borrower_name: BorrowerNameStr
    equipment_id: int=Field(gt=0)
    loan_days: int=Field(gt=0, lt=15)
    purpose: PurposeStr
    #status: 

class LoanRead(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    borrower_name: BorrowerNameStr
    equipment_id: int
    loan_days: int
    purpose: PurposeStr
    #status: 
