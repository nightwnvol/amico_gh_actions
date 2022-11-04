# Install AMICO

Open the system shell and run:

```bash
pip install dmri-amico -U
```

This will download and install AMICO from the [Python Package Index](https://pypi.org).

AMICO is now available in your Python interpreter and can be imported as usual:

```python
import amico
```

# Uninstall AMICO

Open the system shell and run:

```bash
pip uninstall dmri-amico
```
# Dependencies

This version of AMICO is written in [Python](https://www.python.org/) and, internally, it makes use of the [DIPY](http://dipy.org) library.

AMICO fits the models to the data using the [SPArse Modeling Software (SPAMS)](http://spams-devel.gforge.inria.fr).

!!! note
    This implementation of AMICO **does not require** the [NODDI MATLAB toolbox](http://mig.cs.ucl.ac.uk/index.php?n=Download.NODDI) to be present on your system; all the necessary MATLAB functions for generating the response functions of the NODDI model have in fact been ported to Python.
