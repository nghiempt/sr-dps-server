from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes._index import appRouter, categoryRouter, userRouter, userOpinionRouter, infoRouter
from fastapi.openapi.docs import get_swagger_ui_html
app = FastAPI(
    docs_url=None,
    title="Privacy Policy Survey",
    description="This application surveys user opinions about the consistency between Data Safety and Privacy Policy"
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API Document",
        swagger_favicon_url="https://srdps.pfamilies.me/logo_srdps.png"
    )

app.include_router(appRouter,tags=["App"])
app.include_router(categoryRouter,tags=["Category"])
app.include_router(userRouter,tags=["User"])
app.include_router(userOpinionRouter,tags=["Opinion"])
app.include_router(infoRouter,tags=["Information"])
