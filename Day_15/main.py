from typing import Optional
from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()

# Fake "database" — list of employee dicts
employees = [
    {"id": 5, "name": "Eve",    "department": "Marketing",   "active": False},
    {"id": 1, "name": "Anna",   "department": "Engineering", "active": True},
    {"id": 3, "name": "Cathy",  "department": "HR",          "active": True},
    {"id": 2, "name": "Bob",    "department": "Sales",       "active": False},
    {"id": 4, "name": "Diana",  "department": "Engineering", "active": True},
]
@app.get("/")
def root():
    """Root endpoint — shown when you visit just '/'."""
    return {"message": "Hello, FastAPI!"}


@app.get("/hello")
def hello():
    """Says hello back."""
    return {"greeting": "Hello, World!"}


@app.get("/hello/{name}")
def hello_name(name: str):
    """Hello with a personalized name from the URL."""
    return {"greeting": f"Hello, {name}!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "type": str(type(item_id))
    }
    
@app.get("/search")
def search(keyword: str):
    """Search endpoint with REQUIRED query parameter `keyword`."""
    return {"searching_for": keyword}

@app.get("/products")
def list_products(category: str, in_stock: bool):
    """Two query params — both required."""
    return {"category": category, "in_stock": in_stock}

@app.get("/users")
def list_users(skip: int = 0, limit: int = 10, active: bool = True):
    """List users with optional pagination + filter — defaults if not given."""
    return {
        "skip": skip,
        "limit": limit,
        "active": active,
        "message": f"Returning users {skip+1} to {skip+limit} (active={active})"
    }

@app.get("/items")
def list_items(category: Optional[str] = None):
    if category:
        return {"filter": category, "results": "filtered list..."}
    return {"filter": "none", "results": "all items"}

@app.get("/employees")
def list_employees(
    active: Optional[bool] = None,
    department: Optional[str] = None,
    sort: Optional[str] = None
):
    """List all employees, optionally filtered by active status and/or department."""
    results = employees    # start with full list

    if active is not None:
        results = [e for e in results if e["active"] == active]

    if department is not None:
        results = [e for e in results if e["department"].lower() == department.lower()]

    if sort == "name":
        results = sorted(results, key=lambda e: e["name"])
    
    return {"count": len(results), "employees": results}

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    """Get one employee by ID (path param)."""
    for emp in employees:
        if emp["id"] == employee_id:
            return emp
    return {"error": f"Employee {employee_id} not found"}

@app.get("/posts/{post_id}/comments")
def get_comments(post_id:int, limit :int = 5):
    """Get post id (path parameter)"""
    return{
        "post_id": post_id,
        "limit": limit,
        "message": f"Showing {limit} comments for post {post_id}"
    }
    
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    """Get an order by ID."""
    return {"order_id": order_id, "status": "shipped"}


#---------------day 15-------------------
books = [
    {"id": 1, "title": "Atomic Habits",      "author": "James Clear",       "year": 2018, "genre": "Self-help"},
    {"id": 2, "title": "Sapiens",             "author": "Yuval Noah Harari", "year": 2011, "genre": "History"},
    {"id": 3, "title": "Deep Work",           "author": "Cal Newport",       "year": 2016, "genre": "Self-help"},
    {"id": 4, "title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "year": 2011, "genre": "Psychology"},
    {"id": 5, "title": "The Pragmatic Programmer", "author": "Andy Hunt", "year": 1999, "genre": "Tech"},
    {"id": 6, "title": "Clean Code",          "author": "Robert Martin",     "year": 2008, "genre": "Tech"},
]

@app.get("/books")
def list_book(
            genre: Optional[str]= None,
            min_year: Optional[int] = None,
            sort: Optional[str] = None,
            limit: int =10,
):
    """List all books, optionally filtered by title ,genre and/or year."""
    results = books    # start with full list

    if genre is not None:
        results = [b for b in results if genre.lower() in b["genre"].lower()]

    if min_year is not None:
        results = [b for b in results if b["year"] >= min_year]

    if sort == "title":
        results = sorted(results, key=lambda b: b["title"])
    elif sort == "year":
        results = sorted(results, key=lambda b: b["year"])
    
    results = results[:limit]
    return {"count": len(results), "books": results}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Get one book by ID (path param)."""
    for b in books:
        if b["id"] == book_id:
            return b
    return {"error": f"book {book_id} not found"} 