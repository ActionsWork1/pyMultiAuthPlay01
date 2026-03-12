from pydantic import BaseModel


class Address(BaseModel):
    street: str
    building: str
    city: str
    zip: str

class User(BaseModel):
    fname: str
    lname: str
    address: Address

