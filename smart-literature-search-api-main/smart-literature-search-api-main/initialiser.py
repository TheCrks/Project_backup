from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def configureCors(app):
    origins = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
        "https://smart-literature-search-app.vercel.app/"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app