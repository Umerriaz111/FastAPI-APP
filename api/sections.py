import fastapi
router=fastapi.APIRouter()
@router.get("/Sections")
async def readsection():
    return {"Courses": []}


@router.get("/Read_Sections_Content_Block")
async def readsection_Content_Block():
    return {"Courses": []}


@router.get("/Read_Content_Block")
async def readContent_Block():
    return {"Courses": []}
