"""This tests the systems in the settings.py file"""
import pytest
from ben_system.settings import systems

ben_system = systems['ben_pridmore']
system_josh_variation = systems['josh_cohen']


def test_settings_ben_pridmore():
    """All system data are 19 elements long."""
    for k, v in ben_system.items():
        assert len(v) == 19


def test_settings_josh_cohen():
    """All system data are 19 elements long."""
    for k, v in system_josh_variation.items():
        assert len(v) == 19
