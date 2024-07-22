# Sentiment Analysis API

## Overview

This project is a web application built with FastAPI that performs sentiment analysis on user-provided text. The application uses a pre-trained sentiment analysis model from Hugging Face's Transformers library to analyze the sentiment of the text (positive, negative, or neutral) and stores the results in a SQLite database.

## Features

- Input text via a web form
- Analyze the sentiment of the text (positive, negative, or neutral)
- Display the sentiment analysis result on the same page
- Store the analysis results in a SQLite database
- Dockerized setup for easy deployment

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

```bash
SentimentAPI/
    ├── app/
    │   ├── init.py
    │   ├── main.py
    │   ├── models.py
    │   ├── database.py
    │   ├── sentiment_analysis.py
    │   ├── schemas.py
    │   └── templates/
    │       └── index.html
    ├── Dockerfile
    └── docker-compose.yml
```

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/yourusername/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### Build and Run the Docker Container

```bash
docker compose up --build
```
This command will build the Docker image and start the application. The app will be available at http://localhost:8000.

## Usage

1. Open your web browser and go to http://localhost:8000.
2. Enter the text you want to analyze in the text area.
3. Click the "Analyze" button.
4. The sentiment analysis result (positive, negative, or neutral) will be displayed on the same page.