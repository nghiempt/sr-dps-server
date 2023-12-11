from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes._index import appRouter, categoryRouter, userRouter, userOpinionRouter
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(appRouter,tags=["App"])
app.include_router(categoryRouter,tags=["Category"])
app.include_router(userRouter,tags=["User"])
app.include_router(userOpinionRouter,tags=["Opinion"])
