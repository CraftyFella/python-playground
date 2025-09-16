#!/usr/bin/env python3
"""
Hello World Python Workshop Example

This script demonstrates basic Python functionality and verifies
that the dev container environment is working correctly.
"""

import sys
import platform
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from sklearn import __version__ as sklearn_version


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

    # Test data science libraries
    try:
        # NumPy test
        arr = np.array([1, 2, 3, 4, 5])
        print(f"✅ NumPy: array sum = {np.sum(arr)}")

        # Pandas test
        df = pd.DataFrame({'numbers': [1, 2, 3], 'letters': ['a', 'b', 'c']})
        print(f"✅ Pandas: DataFrame shape = {df.shape}")

        # Matplotlib test (create simple plot)
        plt.figure(figsize=(4, 3))
        plt.plot([1, 2, 3], [1, 4, 9])
        plt.title('Test Plot')
        plt.close()  # Close to avoid display issues
        print("✅ Matplotlib: Plot creation working")

        # SciPy test
        print(f"✅ SciPy: Version {scipy.__version__}")

        # Scikit-learn test
        print(f"✅ Scikit-learn: Version {sklearn_version}")

    except ImportError as e:
        print(f"❌ Data science library test failed: {e}")
    except Exception as e:
        print(f"❌ Data science test error: {e}")

    print("=" * 50)
    print("🎉 Workshop environment is ready!")
    print("All data science libraries are working correctly!")
    print("You can now start building amazing Python applications!")


if __name__ == "__main__":
    main()