import os
import sys
import pytest

rootDir = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.insert(0, rootDir)
os.chdir(rootDir)
from app import graph_schemas as gs


@pytest.fixture(scope="session")
def graph_schemas():
    return gs
