# mypy-plugins Examples

Example repository demonstrating the mypy plugins developed by Diego J. Romero-Lopez.

## Overview

This repository contains examples showing how to use the `mypy-pure` and `mypy-raise`
plugins to enforce functional purity in Python code. mypy-pure detects side effects in functions marked with the `@pure` decorator. `mypy-raise` detects functions that raise exceptions.

## Installation

```bash
# Clone the repository
git clone https://github.com/diegojromerolopez/mypy-plugins-examples.git
cd mypy-plugins-examples

# Install dependencies
uv sync
```

## Examples

### mypy-pure examples

#### Valid Pure Functions

[`examples/pure/valid_pure.py`](examples/pure/valid_pure.py) demonstrates correct usage of the `@pure` decorator with functions that have no side effects.

#### Invalid Pure Functions

[`examples/pure/invalid_pure.py`](examples/pure/invalid_pure.py) demonstrates violations that are caught by the plugin.

### mypy-raise examples

#### Valid Raise Functions

[`examples/raise/valid_raise.py`](examples/raise/valid_raise.py) demonstrates correct usage of the `@raise` decorator with functions that raise exceptions.

#### Invalid Raise Functions

[`examples/raise/invalid_raise.py`](examples/raise/invalid_raise.py) demonstrates violations that are caught by the plugin.

## Running the Examples

```bash
# Install dependencies
uv sync

# Check all examples
uv run mypy examples

# Check specific file
uv run mypy examples/pure/valid.py # all valid
uv run mypy examples/pure/invalid.py # mypy-pure errors
uv run mypy examples/raise/valid.py # all valid
uv run mypy examples/raise/invalid.py # mypy-raise errors
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Related Projects

- [mypy-pure](https://github.com/diegojromerolopez/mypy-pure) - The mypy plugin for enforcing function purity.
- [mypy-raise](https://github.com/diegojromerolopez/mypy-raise) - The mypy plugin for informing that a function raises exceptions.
