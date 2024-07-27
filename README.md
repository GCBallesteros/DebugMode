<h1 align="center">
  Debug Mode
</h1> 

<h4 align="center">
  <p>Superpowers when you need them the most</p>
</h4>

Debug mode is a tiny library that puts at your fingertips powerful tools to
debug your code. 

## What you get

If `debug_mode` is activated (see below) you will have the following functions accessible
from everywhere:

- `ic` from the [icecream](https://github.com/gruns/icecream) library. A much
better print statement for debugging purposes.
- `iex` a function decorator from [ipdb](https://github.com/gotcha/ipdb) that
will start a debugger session if the decorated function raises an exception.
Great for those times when you don't know exactly where things are going wrong.

On top of that, when you go start the debugger with `breakpoint()` or
`set_trace()` you will drop into [ipdb](https://github.com/gotcha/ipdb), a much
better pdb and you will have available [wat](https://github.com/igrek51/wat) to
inspect all your variables in a much more powerful way.

Lastly, `debug_mode` will create a folder in the current directory named
`_debug` and will store it's path under the name `debug_folder` and make it
globally accessible.

## Usage

To use it simply import it and export the `DBG` environment variable.

On your code you would normally have the following line sitting there and doing
nothing. 

```python
import debug_mode
```

This has zero overhead and truly does nothing. However, 🐛 __BUG ALERT__ 🐛, now
you need all the help that you can get to sort things out. To activate
`debug_mode` all you need to do is export `DBG`, it can hold any value, it just
needs to be there. You could accomplish this in many ways. 

On your current terminal you could do:
```
export DBG=1
```

and all subsequent runs of your code would activate debug mode. Otherwise you
could use it only for the next invocation of your script:

```
DBG=1 python myscript.py
```

or if you want it always on you could export from your `bashrc`, `zshrc`...


## Making Ruff happy

I personally use Ruff for all my linting. Understandably he is not to happy
about all those global objects that he knows nothing about and will shout out
you, e.g for using "undefined" `ic`.

You can add the following Ruff configuration to your `pyproject.toml`

```toml
[tool.ruff]
builtins = ["ic", "iex"]
```

If you already have a `[tool.ruff]` section on your pyproject just add the
builtins part.

## Installation

Debug mode will be available in pypi soon. In the meantime you may just copy
the `debug_mode` folder into your project and add it's requirements to your
project.

```
pip install icecream ipdb wat-inspector
```

## Credits

Please leave a ⭐ if you find this useful in your projects.
