from http import HTTPStatus

from fastapi import APIRouter

from app.interfaces.schemas import UserPublicSchema, UserSchema

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublicSchema
)
def create_user(user: UserSchema) -> UserPublicSchema:
    pass
