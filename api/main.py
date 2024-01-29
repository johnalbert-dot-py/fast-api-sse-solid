from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SQLModel

# routes
from user.route import router as user_router
from post.route import router as post_router


def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


# SQLModel.metadata.create_all(engine)
# app = FastAPI(lifespan=lifespan)
app = FastAPI()

# middlewares

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
app.include_router(user_router)
app.include_router(post_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
