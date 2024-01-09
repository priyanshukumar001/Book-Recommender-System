from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils import recommend, books_pivot

app = FastAPI()
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
app.mount("/img", StaticFiles(directory="img"), name="img")

templates = Jinja2Templates(directory="static/")


@app.get("/")
def homepage(request: HTMLResponse):
    return templates.TemplateResponse({"request": request}, name="index.html", context={"books_list": list(books_pivot.index)})



@app.post("/", response_class=HTMLResponse)
async def generate_recommendation(request: HTMLResponse, count: str = Form(...), title: str = Form()):
    recommendation_list = recommend(title, int(count))
    print(recommendation_list)
    return templates.TemplateResponse(
        {"request": request}, context={"recommendations": str(recommendation_list[0].tolist()), "title": title, "count": count}, name="final.html" 
    )

# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
