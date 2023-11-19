from .user import router as user_router
from .package import router as package_router
from .apartment import router as apartment_router


def register_routes(app):
    app.include_router(user_router, tags=["user"], prefix="/user")
    app.include_router(package_router, tags=["package"], prefix="/package")
    app.include_router(apartment_router, tags=["apartment"], prefix="/apartment")
