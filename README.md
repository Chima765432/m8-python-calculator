# FastAPI Calculator

A calculator that runs as a web application. FastAPI serves a page with two
inputs and four buttons; each button sends the numbers to an API endpoint,
the server does the math and sends the result back as JSON, and the page
shows it. Invalid input, like a missing number or dividing by zero, returns
a clean error message instead of crashing.

## How it works

The math lives in app/operations as four plain functions. main.py wraps
each one in a POST endpoint: /add, /subtract, /multiply, and /divide.
Requests are validated with Pydantic before the math runs, so bad input
is rejected with a 400 and a message. Every operation and every error is
logged on the server.

## Testing

The suite has three levels:

- Unit tests hit the four functions directly.
- Integration tests send requests to the API in memory, including invalid
  input: missing fields, wrong types, an empty body.
- End-to-end tests use Playwright to drive a real browser: fill the inputs,
  click each button, and check the result on the page.

GitHub Actions runs all of it on every push.

## Setup

    git clone https://github.com/Chima765432/m8-python-calculator.git
    cd m8-python-calculator
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium

## Run it

    python main.py

Then open http://127.0.0.1:8000 in a browser.

## Run the tests

    pytest

Runs all three levels with coverage on the operations module.
