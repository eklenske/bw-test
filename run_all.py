"""
This is a helper script that runs all parts of the pipeline locally and
without a kubernetes cluster. This can be handy for debugging.

NOTE: This file is maintained manually. If you add or remove stages, you'll have
to update this file to reflect your changes.
"""

import multiprocessing
import runpy
import time

import mock

if __name__ == "__main__":

    # The first stage needs arguments, so we mock-patch them
    with mock.patch("sys.argv", ["", "Hello", "World"]):
        try:
            # stage_one.main.main()
            runpy.run_module("stage_one.main", run_name="__main__")
        # We don't want the script to end when sys.exit is called, so we catch it.
        except SystemExit:
            pass

    # The second stage is pretty boring, nothing fancy except for mocking __name__ to __main__.
    runpy.run_module("stage_two.main", run_name="__main__")

    # The third stage spawns a server process. We want this to start (so that all code is run),
    # but after some time we need this to terminate, so that it doesn't block GitHub Actions.
    proc = multiprocessing.Process(
        target=runpy.run_module, args=["stage_three.main"], kwargs={"run_name": "__main__"}
    )
    proc.start()
    time.sleep(5)
    proc.terminate()
    time.sleep(5)
    if proc.is_alive():
        proc.kill()
