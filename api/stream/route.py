from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from sse_starlette.sse import EventSourceResponse
from post.services import get_all_posts
import asyncio, json
import uuid


router = APIRouter(
    prefix="/stream",
    tags=["stream"],
    responses={404: {"description": "Not found"}},
)

STREAM_DELAY = 5  # second
RETRY_TIMEOUT = 15000  # milisecond

users = {}


@router.get("/")
async def stream(request: Request, id: str):
    def new_messages():
        # Add logic here to check for new messages
        # return messages
        posts = get_all_posts(as_dict=True)
        if id not in users:
            users[id] = posts
            yield posts

        if users[id] != posts:
            users[id] = posts
            yield posts
        return

    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if new_messages():
                try:
                    yield {
                        "event": "new_posts",
                        "id": id,
                        "retry": RETRY_TIMEOUT,
                        "data": json.dumps(next(new_messages())),
                    }
                except StopIteration:
                    pass

            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(event_generator())
