# Common
import os
from typing import Optional
current_dir = os.getcwd()


# Framework
from framework.HybridTaxonomyFramework import HybridTaxonomyFramework

workspace = f"{current_dir}/workspaces/all-MiniLM-L6-v2_lr_faiss"

fx = HybridTaxonomyFramework()
fx.setup.workspace = workspace
fx.data.setup.sqlite_attach_file = "/mnt/d/Workspaces/HybridTaxonomyFramework____/data/amazon/extracts/Amazon Products.db"
fx.data.setup.workspace = workspace
fx.labeler.setup.workspace = workspace
fx.embedder.setup.workspace = workspace
fx.classifier.setup.workspace = workspace


fx.initialize()


# Server
from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.responses import FileResponse # type: ignore
from fastapi.encoders import jsonable_encoder # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()
app.mount("/assets", StaticFiles(directory="web/assets"), name="assets")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return FileResponse(os.path.join(os.path.dirname(__file__), "templates/index.html"))
    # return FileResponse(os.path.join(os.path.dirname(__file__), "index.html"))

@app.get("/recommend")
@app.post("/recommend")
def recommend(label_id: Optional[int] = None, text: Optional[str] = None):
    items = fx.recommend(text)
    return items
    pass

@app.get("/categories")
@app.post("/categories")
def categories():
    label_name_mappings = fx.data.load_label_name_mappings()
    categories = []
    for id, name in label_name_mappings.items():
        categories.append({"id": id, "name":name})
    
    return categories

@app.get("/histories")
@app.post("/histories")
def histories():
    print("histories")
    # items = []
    # if request is None or request.query is None:
    #     return items

    # items = fx.recommend(request.query)
    # return items
    return{}
    pass



