"""This tests the systems in the settings.py file"""
import pytest
from ben_system.settings import systems

ben_system = systems['ben_pridmore']
system_josh_variation = systems['josh_cohen']


def test_settings_josh_cohen():
    for k, v in system_josh_variation.items():
        print(k, v)
        assert len(v) == 19
