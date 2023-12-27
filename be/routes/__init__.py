from .users import router as user_router
from .cars import router as car_router
# from .packages import router as package_router
# from .apartments import router as apartment_router
# from .payments import router as payment_router


def register_routes(app):
    app.include_router(user_router, tags=["users"], prefix="/users")
    app.include_router(car_router, tags=["cars"], prefix="/cars")
    # app.include_router(package_router, tags=["packages"], prefix="/packages")
    # app.include_router(apartment_router, tags=["apartments"], prefix="/apartments")
    # app.include_router(payment_router, tags=["payments"], prefix="/payments")
