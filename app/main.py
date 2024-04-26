from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

# Configure templates directory (adjust path as needed)
templates = Jinja2Templates(directory="templates")

# Create the FastAPI application with templates dependency
app = FastAPI(templates=templates)


@app.get("/")
async def read_root(request: Request):
    # Pass context data to the template for dynamic rendering
    context = {"request": request, "title": "Simple Page"}
    return templates.TemplateResponse("index.html", context=context)
