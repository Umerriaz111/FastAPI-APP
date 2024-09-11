import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def readcourses():
    return {"Courses": []}


@router.post("/courses")
async def createcourses():
    return {"Courses": []}


@router.post("/course{id}")
async def addcourseid():
    return {"Courses": []}


@router.patch("/course{id}")
async def patchcourseid():
    return {"Courses": []}


@router.delete("/course{id}")
async def deletecourseid():
    return {"Courses": []}
