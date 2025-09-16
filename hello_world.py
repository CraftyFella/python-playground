#!/usr/bin/env python3
"""
Hello World Python Workshop Example

This script demonstrates basic Python functionality and verifies
that the dev container environment is working correctly.
"""

import sys
import platform
import requests


def main():
    """Main function to demonstrate Python features."""
    print("🐍 Hello from Python Workshop!")
    print("=" * 50)

    # Display Python version and platform info
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Python executable: {sys.executable}")

    # Test external library functionality
    try:
        response = requests.get("https://httpbin.org/json", timeout=5)
        if response.status_code == 200:
            print("✅ Network connectivity: Working")
            print("✅ Requests library: Working")
        else:
            print(f"❌ Network test failed with status: {response.status_code}")
    except Exception as e:
        print(f"❌ Network test failed: {e}")

    # Simple calculation
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"✅ Basic math: sum({numbers}) = {total}")

    # List comprehension example
    squares = [x**2 for x in numbers]
    print(f"✅ List comprehension: squares = {squares}")

    print("=" * 50)
    print("🎉 Workshop environment is ready!")
    print("You can now start building amazing Python applications!")


if __name__ == "__main__":
    main()