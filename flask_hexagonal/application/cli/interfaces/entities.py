from typing import Dict, Optional, List, Union

from pydantic import BaseModel


class CmdError(BaseModel):

    message: str
    type: str
    details: Optional[Dict[str, str]] = {}


class CmdResponse(BaseModel):

    data: Optional[Union[BaseModel, List[BaseModel]]] = None
    error: Optional[CmdError] = None
