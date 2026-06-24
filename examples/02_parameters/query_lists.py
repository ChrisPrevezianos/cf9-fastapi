from typing import Annotated
from fastapi import FastAPI, Query
 
app = FastAPI(
    title="Query Lists & Booleans",
    description=(
        "Demonstrates list query parameters, optional query parameter,"
        "and automatic boolean/number coversion in FastAPI"
    ),
    version="1.0.3"
)
 
@app.get("/products")
def products(tags: Annotated[list[str] | None, Query()] = None,
             min_price: Annotated[float, Query(description="Minimun product price", examples=[9.99])] = 0,
             on_sale: bool = False # make it with Annotated! HW!
):
    return {
        "tags": tags,
        "min_price": min_price,
        "on_sale": on_sale
    }