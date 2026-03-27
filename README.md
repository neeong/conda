# Conda environment with environment.yml

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/conda_environment/master?filepath=index.ipynb)

A Binder-compatible repo with an `environment.yml` file.

Access this Binder by clicking the blue badge above or at the following URL:

http://mybinder.org/v2/gh/binder-examples/conda_environment/master?filepath=index.ipynb

## Notes
The `environment.yml` file should list all Python libraries on which your notebooks
depend, specified as though they were created using the following `conda` commands:

```
source activate example-environment
conda env export --no-builds -f environment.yml
```

Note that the only libraries available to you will be the ones specified in
the `environment.yml`, so be sure to include everything that you need! 

Also note that conda will possibly try to include OS-specific packages in `environment.yml`, so you
may have to manually prune `environment.yml` to get rid of these packages. Confirmed Mac-OSX-specific
packages that should be removed are:

* libcxxabi=4.0.1
* appnope=0.1.0
* libgfortran=3.0.1
* libcxx=4.0.1

## Running Python on iPhone

There are several ways to use this environment or run Python notebooks on an iPhone.

### Option 1: Use Binder in a Mobile Browser

The simplest approach — no installation needed:

1. Tap the Binder badge at the top of this README (or visit the Binder URL above).
2. Wait for the environment to build and launch in your browser.
3. Open `index.ipynb` to run the notebook.

Works in Safari and Chrome on iOS.

### Option 2: Carnets (Jupyter Notebooks for iOS)

[Carnets](https://holzschu.github.io/Carnets_Jupyter/) is a free Jupyter notebook app for iPhone and iPad.

1. Install Carnets from the App Store.
2. Download the notebooks from this repo (tap a `.ipynb` file on GitHub → Raw → Save to Files).
3. Open the notebook in Carnets.

Note: Carnets runs a local Python kernel and supports many packages via pip, but does not support conda. Install required packages manually:

```
pip install numpy pandas matplotlib dask toolz bokeh partd psutil dill
```

### Option 3: a-Shell (Terminal on iOS)

[a-Shell](https://holzschu.github.io/a-Shell_iOS/) is a terminal app for iOS that includes Python.

1. Install a-Shell from the App Store.
2. Install required packages:

```sh
pip install numpy pandas matplotlib dask toolz bokeh partd psutil dill
```

3. Transfer your `.py` scripts via Files and run them with `python script.py`.

### Option 4: SSH into a Remote Server

If you have access to a remote Linux server or cloud VM with conda installed:

1. Use an SSH client such as [Blink Shell](https://blink.sh/) or [Termius](https://termius.com/).
2. Connect to your server and activate the environment:

```sh
conda env create -f environment.yml
conda activate example-environment
jupyter notebook --no-browser
```

3. Forward the Jupyter port to your device using SSH port forwarding, then open `localhost:8888` in Safari.
