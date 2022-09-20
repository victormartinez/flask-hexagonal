from typing import Dict, Optional

from pydantic import BaseModel


class CmdError(BaseModel):

    message: str
    type: str
    details: Optional[Dict[str, str]] = {}


class CmdResponse(BaseModel):

    data: Optional[BaseModel] = None
    error: Optional[CmdError] = None
