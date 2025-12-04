# Behave BDD UI + API Tests

This project contains example automation using **Behave (Python BDD)**:

- ✅ API tests against JSONPlaceholder (`/posts`)
- ✅ UI tests for [saucedemo.com](https://www.saucedemo.com) using Selenium
- ✅ Tagged scenarios: `@api`, `@ui`, `@smoke`, `@regression`
- ✅ Conditional browser setup via `environment.py`

## Run tests

Create and activate a virtual environment, then:

```bash
pip install -r requirements.txt   
behave                # run all tests
behave --tags=@api    # only API tests
behave --tags=@ui     # only UI tests
