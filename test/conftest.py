"""Globally available test fixtures"""
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def harringtons_html():
    this_dir = Path(__file__).parent
    harringtons_html = this_dir / 'data' / 'harrington-sales.html'
    return harringtons_html.read_text()
