
from api import user,courses,sections
from fastapi import FastAPI
app=FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Umer Riaz",
        "email": "Umerriaz2334@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)
app.include_router(user.router)
app.include_router(courses.router)
app.include_router(sections.router)