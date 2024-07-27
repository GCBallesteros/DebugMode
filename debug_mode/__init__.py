from pathlib import Path
import os

if "DBG" in os.environ:
    import icecream
    import wat
    from ipdb import iex

    icecream.ic.configureOutput(includeContext=True)

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
