# triton-ci
CI scripts designed to build a Pascal-compatible version of Triton. 

*I plan to publish this version of `triton` on PyPI as soon as the [file size limit increase request](https://github.com/pypi/support/issues/4295) is approved.*

Install application that published on PyPI and depends on `triton`:
```sh
# Install triton
pip3 install --extra-index-url https://sasha0552.github.io/triton-ci/ <PACKAGE NAME>
```

Install `triton` before installing application:
```sh
# Install triton
pip3 install --extra-index-url https://sasha0552.github.io/triton-ci/ triton==<VERSION>
```

If application is already installed:
```sh
# Install triton
pip3 install --index-url https://sasha0552.github.io/triton-ci/ --force-reinstall --no-deps triton
```

*Don't forget to activate the virtual environment (if necessary) before performing actions!*
