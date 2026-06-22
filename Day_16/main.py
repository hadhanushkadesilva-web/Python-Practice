from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Create the FastAPI app instance
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

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


#----------------day 16---------------

@app.post("/items-new")
def create_item(item: Item):
    """Accept a JSON item and echo it back with confirmation."""
    return {
        "created": item,
        "message": f"Item '{item.name}' added at ${item.price}",
        "in_stock": item.in_stock
    }
    
class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0, le=10000)
    category: str = Field(default="Uncategorized", min_length=2)

@app.post("/products-new")
def create_product(product: Product):
    """Accept a Product with validation."""
    total_value = product.price * product.quantity
    return {
        "received": product,
        "total_inventory_value": total_value,
        "message": f"Product '{product.name}' added to {product.category}"
    }
    
class UserSignup(BaseModel):
    name: str = Field(..., min_length=2)
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    password: str = Field(..., min_length=8)
    age: int = Field(..., ge=13)

class UserPublic(BaseModel):
    name: str
    email: str
    age: int
    # NOTICE: NO password field

@app.post("/signup", response_model=UserPublic)
def signup(user: UserSignup):
    """Sign up a new user. Password is accepted but NEVER returned."""
    # In a real app: hash password, save to DB, etc.
    print(f"Saving user {user.name} with password '{user.password}' (would be hashed)")
    return user


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    department: str = Field(..., min_length=2)
    salary: float = Field(..., gt=0)
    active: bool = True

class EmployeePublic(BaseModel):
    id: int
    name: str
    department: str
    active: bool
    # NOTICE: salary HIDDEN in response — sensitive!
    
@app.post("/employees", response_model=EmployeePublic, status_code=201)
def create_employee(new_emp: EmployeeCreate):
    """Create a new employee with full validation. Returns sanitized data."""
    # Auto-generate the next ID
    next_id = max(e["id"] for e in employees) + 1 if employees else 1
    
    # Build the new employee dict
    employee = {
        "id": next_id,
        "name": new_emp.name,
        "department": new_emp.department,
        "salary": new_emp.salary,
        "active": new_emp.active,
    }
    
    # Add to our "database"
    employees.append(employee)
    
    return employee