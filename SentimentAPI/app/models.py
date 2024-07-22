from sqlalchemy import Column, Integer, String
from .database import Base

class SentimentAnalysis(Base):
    __tablename__ = "sentiment_analysis"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    sentiment = Column(String, index=True)
