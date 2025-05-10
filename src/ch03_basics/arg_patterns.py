"""Samples covering all major Python argument patterns.

Run this file directly to see console output for each example.
Feel free to tweak values, comment lines in/out, and rerun to deepen understanding.
"""
from __future__ import annotations

def greet(name: str, message: str = "こんにちは") -> None:
    """位置引数 + デフォルト値の組み合わせ例. """
    print(f"{name} さん、{message}")
