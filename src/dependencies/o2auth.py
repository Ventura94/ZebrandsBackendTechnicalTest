from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.constants import ALGORITHMS
from jose.exceptions import JWTClaimsError, ExpiredSignatureError, JWTError

from src.configs.application import get_settings
from src.exceptions.authentication_failed import AuthenticationFailed

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/v1/auth/login", description="authorization"
)


def o2auth(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(
            token,
            get_settings().SECRET_KEY,
            algorithms=ALGORITHMS.HS256,
            audience=get_settings().TOKEN_AUD,
        )
    except JWTClaimsError as exc:
        raise AuthenticationFailed(
            "If any claim is invalid in any way.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    except ExpiredSignatureError as exc:
        raise AuthenticationFailed(
            "If the signature has expired.", headers={"WWW-Authenticate": "Bearer"}
        ) from exc
    except JWTError as exc:
        raise AuthenticationFailed(
            "If the signature is invalid in any way.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    return data
