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

[a-Shell](https://holzschu.github.io/a-Shell_iOS/) is a terminal app for iOS that includes Python 3 and pip.

#### Step 1: Install a-Shell

Install **a-Shell** (free) from the [App Store](https://apps.apple.com/app/a-shell/id1473805438).

#### Step 2: Update pip

Open a-Shell and run:

```sh
pip install --upgrade pip
```

#### Step 3: Install required packages

Install all packages used in this environment:

```sh
pip install numpy pandas matplotlib dask toolz bokeh partd psutil dill
```

Each package and what it is used for:

| Package | Purpose |
|---------|---------|
| `numpy` | Numerical arrays and math |
| `pandas` | Data analysis and DataFrames |
| `matplotlib` | Plotting and visualization |
| `dask` | Parallel and out-of-core computation |
| `toolz` | Functional programming utilities |
| `bokeh` | Interactive web-based plots |
| `partd` | Append-only key-value storage (used by dask) |
| `psutil` | System/process utilities |
| `dill` | Extended pickling/serialization |

#### Step 4: Get the notebooks onto your iPhone

**Option A — clone via a-Shell (recommended):**

```sh
git clone https://github.com/neeong/conda
cd conda
```

**Option B — download manually:**

1. Open this repo on GitHub in Safari.
2. Tap a `.ipynb` file → Raw → tap the share icon → Save to Files → a-Shell Documents.

#### Step 5: Run a script

```sh
cd conda
python -c "import dask; print(dask.__version__)"
```

For interactive use, a-Shell also supports `python3` directly:

```sh
python3
>>> import pandas as pd
>>> pd.DataFrame({'a': [1, 2, 3]})
```

> **Note:** a-Shell does not support Jupyter notebooks natively. For notebooks on-device, use Option 2 (Carnets) instead.

#### Installing Claude Code in a Shell on iPhone

Claude Code is a Node.js CLI tool, so it requires `npm`. a-Shell does not include Node.js, so use one of the two approaches below.

**Option A — iSH (Alpine Linux on iOS)**

[iSH](https://ish.app/) runs a full Alpine Linux environment on iPhone and supports `apk`, `node`, and `npm`.

1. Install **iSH** (free) from the [App Store](https://apps.apple.com/app/ish-shell/id1436902243).
2. Open iSH and install Node.js:

```sh
apk add nodejs npm
```

3. Install Claude Code globally:

```sh
npm install -g @anthropic-ai/claude-code
```

4. Verify the installation:

```sh
claude --version
```

5. Authenticate with your Anthropic API key:

```sh
export ANTHROPIC_API_KEY=your_api_key_here
claude
```

**Option B — SSH into a remote server**

If you have a remote server with Node.js already available:

```sh
# On the remote server
npm install -g @anthropic-ai/claude-code
claude --version
```

Then use it over SSH from any iOS SSH client (Blink Shell, Termius, etc.).

#### Using Claude Code on iPhone (iSH)

Once installed, open iSH every session and set your API key:

```sh
export ANTHROPIC_API_KEY=your_api_key_here
```

To avoid typing this every session, add it to your shell profile:

```sh
echo 'export ANTHROPIC_API_KEY=your_api_key_here' >> ~/.profile
source ~/.profile
```

**Interactive mode** — chat with Claude in the terminal:

```sh
claude
```

Type your question or instruction, press Enter. Type `/exit` or Ctrl+C to quit.

**One-shot mode** — run a single prompt and return to shell:

```sh
claude "explain this error: ModuleNotFoundError: No module named numpy"
claude "write a python function to reverse a string"
```

**Work on a project** — navigate to your repo and let Claude read the code:

```sh
cd /root/conda
claude "what does iphone_demo.py do?"
claude "add error handling to iphone_demo.py"
```

**Useful Claude Code commands inside the session:**

| Command | What it does |
|---------|-------------|
| `/help` | Show all available commands |
| `/clear` | Clear conversation history |
| `/exit` | Exit Claude Code |
| `Ctrl+C` | Cancel current response |

**Limitations on iPhone:**

- iSH emulates x86 on ARM — it is slower than a real terminal
- File access is sandboxed to iSH's own filesystem (`/root`)
- To work on files from a-Shell, copy them into iSH first via the Files app
- No persistent environment variables between sessions (use `~/.profile`)

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
