from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from pydantic import ValidationError
from . import models, database, sentiment_analysis, schemas
from .database import get_db
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Sentiment Analysis API",
    description="A FastAPI application to analyze the sentiment of text input.",
    version="1.0.0"
)

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """
    Render the main page with a form for inputting text to analyze.

    Args:
        request (Request): The incoming request object.

    Returns:
        HTMLResponse: The rendered HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def analyze_text(request: Request, text: str = Form(...), db: Session = Depends(get_db)):
    """
    Analyze the sentiment of the provided text and display the result.

    Args:
        request (Request): The incoming request object.
        text (str): The text to be analyzed.
        db (Session): The database session.

    Returns:
        HTMLResponse: The rendered HTML page with the analysis result or validation errors.
    """
    try:
        # Validate input data using Pydantic
        text_input = schemas.TextInput(text=text)
    except ValidationError as e:
        errors = e.errors()
        return templates.TemplateResponse("index.html", {"request": request, "errors": errors})
    
    # Analyze sentiment
    sentiment = sentiment_analysis.analyze_sentiment(text_input.text)
    # Save result to database
    db_record = models.SentimentAnalysis(text=text_input.text, sentiment=sentiment)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    # Render result
    return templates.TemplateResponse("index.html", {"request": request, "text": text_input.text, "sentiment": sentiment})