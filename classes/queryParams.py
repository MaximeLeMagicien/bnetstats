from pydantic import BaseModel

class queryParams(BaseModel):
    initialAppURL : str = "https://battlenetstats-1-c8631078.deta.app/"
    sessionKey : str = ""
    state : str = ""
    token : str = ""

params = queryParams()