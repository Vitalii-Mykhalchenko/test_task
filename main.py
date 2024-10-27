from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from routers.chatbot import router as chatbot_router


app = FastAPI()

app.include_router(chatbot_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Main page with instructions.

    Returns:
        HTMLResponse: The HTML content of the main page.
    """
    return HTMLResponse(open("templates/index.html").read())
