"""Test utilities that should be commonly found and used in most test cases"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
