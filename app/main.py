from fastapi import FastAPI, Path
from app.routes.book import router as BookRouter
from app.routes.user import router as UserRouter
from app.routes.interactions import router as IntersectionRouter
from .test_data import router as TestRouter
app = FastAPI(debug=True)

app.include_router(BookRouter, tags=["Book"], prefix="/books")
app.include_router(UserRouter, tags=["User"], prefix="/users")
app.include_router(IntersectionRouter, tags=["Intersection"], prefix="/intersections")
app.include_router(TestRouter, tags=["Test"], prefix="/tests")
