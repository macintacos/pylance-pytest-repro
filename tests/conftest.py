import pytest
from fixtures.test_fixtures import mock_fixture

# FIX: Add "python.analysis.extraPaths": ["tests"] to settings
# fixtures.test_fixtures says it cannot be resolved, however it properly _is_ resolved, because the tests run fine
