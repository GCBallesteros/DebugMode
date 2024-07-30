import os
from pathlib import Path
from time import time

if "DBG" in os.environ:
    import icecream
    import wat
    from ipdb import iex

    start_time = time()
    
    def delta_time():
        delta = time() - start_time

        return f"{delta:.2f}s | "

    icecream.ic.configureOutput(includeContext=True, prefix=delta_time)

    # Make ipdb the default debugger
    os.environ["PYTHONBREAKPOINT"] = "ipdb.set_trace"

    debug_folder = Path("./_debug").resolve()
    debug_folder.mkdir(exist_ok=True)

    icecream.install()

    # Add a few things to builtins so that they are
    # always available
    builtins = __import__("builtins")

    setattr(builtins, "wat", wat)
    setattr(builtins, "iex", iex)
    setattr(builtins, "debug_folder", debug_folder)
