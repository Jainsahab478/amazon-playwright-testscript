# Amazon Playwright Tests

This is my submission for the automation assignment. I have written two test cases using Playwright and Python.

## What the tests do

- Test 1 searches for iphone on amazon.in, opens the product and prints the price, then adds it to cart
- Test 2 does the same thing but for samsung galaxy
- Both tests run at the same time (parallel execution) using pytest-xdist

## How to run

First install the required libraries:

```bash
pip install playwright pytest pytest-xdist pytest-playwright
playwright install
```

Then just run:

```bash
pytest -v
```

You should see both tests running together and passing.

## Requirements

- Python 3.9 or above
- Internet connection (it opens a real browser)

## Notes

- I used amazon.in instead of amazon.com since I am based in India
- The browser will open visibly while tests run, that is expected
- Parallel execution is set up in pytest.ini with -n 2
