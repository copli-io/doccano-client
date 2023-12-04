from typing import Dict

from pydantic import BaseModel, root_validator, constr

Password = constr(min_length=2, max_length=128, strip_whitespace=True)

class UserDetails(BaseModel):
    pk: int
    username: str
    email: str
    first_name: str
    last_name: str


class PasswordUpdated(BaseModel):
    detail: str

class PasswordChange(BaseModel):
    new_password: Password
    confirm_password: Password

    @root_validator(pre=False, skip_on_failure=True)
    def new_password_matches_confirm_password(cls, values: Dict[str, Password]):
        new_password = values.get("new_password")
        confirm_password = values.get("confirm_password")
        if new_password != confirm_password:
            raise ValueError("The new password does not match the confirm one.")
        return values
