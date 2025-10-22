
from dataclasses import dataclass


@dataclass
class SysUserResponse:
    id: int
    username: str
    email: str
    full_name: str