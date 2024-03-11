"""Pytest configuration and fixtures for the calculator app tests."""
# tests/conftest.py
import sys
import os
# In your conftest.py or within your test module
import logging
import pytest
from io import StringIO

@pytest.fixture
def log_output():
    log_capture_string = StringIO()
    ch = logging.StreamHandler(log_capture_string)
    ch.setLevel(logging.INFO)
    logging.getLogger().addHandler(ch)
    yield log_capture_string
    logging.getLogger().removeHandler(ch)

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
