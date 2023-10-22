from pydantic import BaseModel

class queryParams(BaseModel):
    initialAppURL : str = "http://127.0.0.1:4200/"
    state : str = ""
    token : str = ""

params = queryParams()