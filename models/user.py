from pydantic import BaseModel, Field
import secrets
from typing import List,Dict

class Account(BaseModel):
    email: str = Field(..., pattern=r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    account_name: str
    website: str = None
    app_secret_token: str = Field(default_factory=lambda: secrets.token_hex(32))

class Destination(BaseModel):
    url: str
    http_method: str
    headers: Dict[str,str]

class Destinations(BaseModel):
    account_id: str
    destination: List[Destination]