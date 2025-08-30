from fastapi import Request
from fastapi.responses import JSONResponse

from media_manager.torrent.schemas import Torrent


class MediaAlreadyExists(Exception):
    """Raised when a show already exists"""

    def __init__(
        self, message: str = "Entity with this ID or other identifier already exists"
    ):
        super().__init__(message)
        self.message = message

    pass


class NotFoundError(Exception):
    """Custom exception for when an entity is not found."""

    def __init__(self, message: str = "The requested entity was not found."):
        super().__init__(message)
        self.message = message

    pass


class TorrentNotFoundError(Exception):
    """Custom exception for when a torrent is not found."""

    def __init__(self, torrent: Torrent):
        super().__init__(f"Torrent was not found with title: '{torrent.title}'")
        self.torrent: Torrent = torrent

    pass


class InvalidConfigError(Exception):
    """Custom exception for when an entity is not found."""

    def __init__(self, message: str = "The server is improperly configured."):
        super().__init__(message)
        self.message = message

    pass


async def media_already_exists_exception_handler(
    request: Request, exc: MediaAlreadyExists | Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"detail": exc.message},
    )


async def not_found_error_exception_handler(
    request: Request, exc: NotFoundError | Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"detail": exc.message},
    )


async def invalid_config_error_exception_handler(
    request: Request, exc: InvalidConfigError | Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"detail": exc.message},
    )


async def sqlalchemy_integrity_error_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={
            "detail": "The entity to create already exists or is in a conflict with others."
        },
    )
