# Setup

1. Open the project in VSCode (make sure you're using Pylance, and it's configured correctly)
2. Do the following:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -e .

# make sure that you tell VSCode to use this new virtual environment

$ python src/app.py
Here's some data returned: ['some data']

$ pytest -k tests test_pylance.py -v
# test output... (check out the test, we're actually returning the fixture)
```