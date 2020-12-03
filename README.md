# Setup

1. Open the project in VSCode
2. Do the following:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -e .

$ python src/app.py
Here's some data returned: ['some data']

$ pytest -k tests test_pylance.py -v
# test output... (check out the test, we're actually returning the fixture)
```