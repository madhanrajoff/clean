from .users import router as user_router
from .packages import router as package_router
from .apartments import router as apartment_router


def register_routes(app):
    app.include_router(user_router, tags=["users"], prefix="/users")
    app.include_router(package_router, tags=["packages"], prefix="/packages")
    app.include_router(apartment_router, tags=["apartments"], prefix="/apartments")
