"""Tests for the RecentCounter class."""

import importlib.util
from pathlib import Path


def _load_module():
    """Load the RecentCounter module despite the non-standard filename."""

    module_path = Path(__file__).with_name("933-number-of-recent-calls.py")
    spec = importlib.util.spec_from_file_location("recent_counter", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def test_recent_counter_basic():
    module = _load_module()
    rc = module.RecentCounter()

    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3


def test_recent_counter_sliding_window():
    module = _load_module()
    rc = module.RecentCounter()

    times = [1, 100, 3001, 3002, 6000]
    results = [rc.ping(t) for t in times]
    # At t=6000, the window [3000, 6000] still contains the three most recent timestamps
    assert results == [1, 2, 3, 3, 3]

