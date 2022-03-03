"""
This is a helper script that runs all parts of the pipeline locally and
without a kubernetes cluster. This can be handy for debugging.

NOTE: This file is maintained manually. If you add or remove stages, you'll have
to update this file to reflect your changes.
"""

import unittest.mock

import stage_one.main
import stage_two.main

if __name__ == "__main__":
    # The first stage needs arguments, so we mock-patch them
    with unittest.mock.patch("sys.argv", ["", "Hello", "World"]):
        try:
            stage_one.main.main()
        # We don't want the script to end when sys.exit is called, so we catch it.
        except SystemExit:
            pass

    stage_two.main.main()
