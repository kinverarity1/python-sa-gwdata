import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import logging

import pytest

test_dir = os.path.dirname(__file__)

example_file = lambda fn: os.path.join(os.path.dirname(__file__), 'examples', fn)

logger = logging.getLogger(__name__)
