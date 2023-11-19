from .users import router as user_router


def register_routes(app):
    app.include_router(user_router, tags=["users"], prefix="/user")
