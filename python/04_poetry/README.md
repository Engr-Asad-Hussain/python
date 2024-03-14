## Poetry
`Poetry` helps you create new projects or maintain existing projects while taking care of dependency management for you. Poetry can also help you build a `distribution package` for your project. If you want to share your work, then you can use Poetry to publish your project on the Python Packaging Index (PyPI).


## Content
- [Install poetry](#1-install-poetry-on-your-computer)
  - [Difference between pip and pipx](#11-difference-between-pip-and-pipx)
  - [Recommended way to install poetry](#12-recommended-way-to-install-poetry)
- [Start a project with poetry](#2-start-a-project-with-poetry)
  - [Understand the pyproject.toml file](#21-understand-the-pyprojecttoml-file)
  - [Poetry virtual environment](#22-poetry-virtual-environment)
  - [Declare runtime dependencies](#23-declare-runtime-dependencies)
  - [Remove runtime dependencies](#24-remove-runtime-dependencies)
  - [Group dependencies](#25-group-dependencies)
  - [Extra dependencies](#26-extra-dependencies)
  - [Remove poetry virtual environment](#27-remove-poetry-virtual-environment)
  - [Poetry configurations](#29-poetry-configurations)
  - [Activate virtuale environment](#210-activate-virtuale-environment)
  - [Run packages from virtual evironment](#211-run-packages-from-virtual-evironment)
- [Install dependencies with poetry](#3-install-dependencies-with-poetry)
- [Manage dependencies manually](#4-manage-dependencies-manually)
  - [Lock dependencies](#41-lock-dependencies)
  - [Purpose of poetry lock](#42-purpose-of-poetry-lock)
- [Add poetry to an existing project](#5-add-poetry-to-an-existing-project)
- [Install poetry with pip](#6-install-poetry-with-pip)

## 1. Install poetry on your computer
- Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system. 
- You also want to install Poetry system-wide to access it as a stand-alone application regardless of the specific virtual environment or Python version that you’re currently working in.


#### 1.1. Difference between pip and pipx
- **pip**:
  - Pip is the default package manager for Python.
  - When you install a package using pip, it installs the package and its dependencies globally in the Python environment.
  - This means that the installed package is available system-wide, and any Python script or project can use it.
  - List dependencies `pip list`.
  - To install poetry using pip: `pip install poetry`
- **pipx**
  - Pipx is a tool that provides a way to install and run Python packages in isolated environments, called "virtual environments".
  - It installs packages in a way that makes them available globally for execution without polluting the global Python environment.
  - List dependencies `pipx list`.
  - To install poetry using pipx: `pipx install poetry`


#### 1.2. Recommended way to install poetry
- The recommended way to install Poetry is with the help of `pipx`, which takes care of creating and maintaining isolated virtual environments for command-line Python applications. To install pipx and poetry folow the official [docs](https://python-poetry.org/docs/).
- Get all the dependencies in pipx virtual environment: `pipx list`.

## 2. Start a project with poetry
To create a new Poetry project from scratch, use the `poetry new` command followed by the desired project name.
```bash
poetry new rp-poetry
cd rp-poetry/
```
You’ll see the following structure:
```
rp-poetry/
│
├── rp_poetry/
│   └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── README.md
└── pyproject.toml
```
- The subfolder/package will be created with underscore (_) to make sure `rp_poetry` would be valid Python package that can easly be import.
- Provide custom project name with `--name` flag example `poetry new rp-poetry --name real_poetry`


### 2.1. Understand the pyproject.toml file
When you start a new poetry project it will create following `pyproject.toml` file.
```toml
[tool.poetry]
name = "rp-poetry"
version = "0.1.0"
description = ""
authors = ["Philipp Acsany <philipp@realpython.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

- The sections denoted with square brackets are know as `tables` in `TOML` terminology.
- **[tool.poetry]** table is where you can store project's metadata.
- **[tool.poetry.dependencies]** table is where you specify external dependencies.
- **[build-system]** table contains obligatory build requirements for your project.

In this case, the two subtables belong to only one external tool—Poetry. But you’ll often find examples like **[tool.black]**, **[tool.isort]**, **[tool.mypy]**, or **[tool.pytest.ini_options]** for their corresponding tools.


### 2.2. Poetry virtual environment
- When you create a new Python project by hand, it’s a good practice to also create an associated virtual environment (`virtualenv venv`). 
- Poetry comes with built-in support for virtual environments.
- However, Poetry doesn’t create a virtual environment right away when you start a new project. That’s by design to let you decide whether you want to manage your virtual environments yourself or let Poetry handle them for you automatically.
- Poetry will detect a manually activated virtual environment when you run one of the Poetry commands in your project’s folder:
```bash
cd rp-poetry/
poetry env info --path
```

> In other words, if you now tried adding dependencies to your project through Poetry, you’d install them into the activated environment as if with the regular pip install command.

> On the other hand, Poetry will automatically creates a virtual environment when you add or remove a dependency using poetry's command-line interface. Letting Poetry create virtual environments on its own is the preferred way of isolating dependencies in your projects. Poetry constructs a unique name for your virtual environment by adding `base64-encoded hash` value of you projects parent directory path. Poetry creates virtual environments in the `virtualenvs/` subfolder of its cache directory, which is specific to the operating system. To reveal your current Poetry configuration, which includes the cache-dir and virtualenvs.path settings, run this command: `poetry config --list`


### 2.3. Use poetry’s virtual environments
You can list all virtual environments that Poetry manages. Whenever you install any package using poetry command-line, it will automatically create the virtual environment for that project.
```bash
poetry env list
```


### 2.4. Declare runtime dependencies
Running the poetry add command will automatically update your `pyproject.toml` file with the new dependency and install the package at the same time. In fact, you can even specify multiple packages in one go:
```bash
poetry add requests==2.25.1 beautifulsoup4
```
```toml
[tool.poetry]
name = "rp-poetry"
version = "0.1.0"
description = ""
authors = ["Philipp Acsany <philipp@realpython.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.31.0"
beautifulsoup4 = "^4.12.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
> Note the caret symbol (^) before the version specifiers, which indicates that Poetry is free to install any version matching the leftmost non-zero digit of the version string. For example, if the Requests library releases a new version 2.99.99, then Poetry will consider it an acceptable candidate for your project. However, version 3.0 wouldn’t be allowed.


### 2.5. Remove runtime dependencies
If you want to remove one or more dependencies from your project, then Poetry provides the related poetry remove command: 
```bash
poetry remove requests
```

> As you can see, it’ll remove the given dependency along with its transitive dependencies, so you don’t need to worry about leftover packages that are no longer needed by your project. This is an advantage of Poetry over plain `pip`, which can only uninstall the individual packages.


### 2.6. Group dependencies
You can create group dependencies like `development`, `testint`, `staging` which is missing from pip.
```bash
poetry add --group dev black flake8 isort mypy pylint
poetry add --group test pytest faker
```

Resulting in `[tool.poetry.group.dev.dependencies]` and `[tool.poetry.group.test.dependencies]` groups:
```toml
[tool.poetry.group.dev.dependencies]
black = "^24.1.1"
flake8 = "^7.0.0"
isort = "^5.13.2"
mypy = "^1.8.0"
pylint = "^3.0.3"

[tool.poetry.group.test.dependencies]
pytest = "^8.0.0"
faker = "^22.6.0"
```


### 2.7. Extra dependencies
You can define optional dependencies and groups by setting the corresponding attribute in the `pyproject.toml` file. For example, this declaration will turn your test group into an optional one:
```toml
[tool.poetry.group.test]
optional = true

[tool.poetry.group.test.dependencies]
pytest = "^8.0.0"
faker = "^22.6.0"
```

> Poetry won’t install dependencies belonging to such a group unless you explicitly instruct it to by using the `--with` option. In addition to this, you can add the individual packages as optional to let the user choose whether to install them:
```bash
poetry add --optional mysqlclient psycopg2-binary
```
```toml
[tool.poetry.dependencies]
mysqlclient = {version = "^2.2.1", optional = true}
psycopg2-binary = {version = "^2.9.9", optional = true}
```

However, this isn’t enough to expose such optional dependencies to the user. You must also define extras in your pyproject.toml file, which are sets of optional dependencies that your users can install together:
```toml
[tool.poetry.extras]
databases = ["mysqlclient", "psycopg2-binary"]
mysql = ["mysqlclient"]
pgsql = ["psycopg2-binary"]
```


### 2.8. Remove poetry virtual environment
Get the list of all virtual environments:
```bash
poetry env list
```
Get the information about virtual environment relative to the project:
```bash
poetry env info --path
```
Remove the poetry virtual environment:
```bash
poetry env remove rp-poetry-CEUO-QFO-py3.11
```


### 2.9. Poetry configurations
You can check the default configurations of poetry using following command:
```bash
poetry config --list
```

The best practice is to create the virtualenv inside the project’s root directory. By default poetry will create virtual environment at `{cache-dir}/virtualenv`. To configure project based virtual environments change the default configurations using:
```bash
poetry config virtualenvs.in-project true
```


### 2.10. Activate virtuale environment
You can activate the poetry virtual environment using following command:
```bash
poetry shell
```
You can deactivate this environment via `deactivate` command.


### 2.11. Run packages from virtual evironment
The run command executes the given command inside the project's virtualenv. It can also execute one of the scripts defined in pyproject.toml.
```bash
poetry run python --version
```
You can deactivate this environment via `deactivate` command.


## 3. Install dependencies with poetry
Imagine that you’ve just cloned a Git repository with the `rp-poetry` project from `GitHub` and are starting fresh with no virtual environment. To install dependencies you can run command: 
```bash
poetry install
```

- It will create a virtual environment and install the dependencies listed in pyproject.toml.
- By default, Poetry installs dependencies from the implicit main group as well as all dependency groups i.e., [tool.poetry.dependencies], [tool.poetry.group.dev.dependencies], [tool.poetry.group.test.dependencies] but it will not install dependencies with `optional = true`.

> If other contributors have committed the `poetry.lock` file to the remote repository, which they generally should, then Poetry will read that file. It’ll reproduce the exact same environment on your machine with identical versions of all the dependencies listed in the most recent snapshot of `poetry.lock`.

> Otherwise, Poetry will fall back to reading the top-level dependencies outlined in the pyproject.toml file and will resolve the set of packages satisfying the version constraints. As a result, you’ll have a new local poetry.lock file.


In contrast, Poetry won’t automatically install extra sets of dependencies and optional groups of dependencies. To get those, you must use some of the following parameters:
```bash
--all-extras
--extras {extra}
--with {optional groups}
```
```bash
poetry install --extras databases
# Result in installation of ["mysqlclient", "psycopg2-binary"]
```


## 4. Manage dependencies manually
Whenever you interact with Poetry through its command-line interface, it updates the `pyproject.toml` file and pins the resolved versions in the `poetry.lock` file. However, you don’t have to let Poetry do all the work. You can manually modify dependencies in the pyproject.toml file and lock them afterward.


### 4.1. Lock dependencies
The `poetry.lock` file is not meant to be changed by hand, you can edit the related `pyproject.toml` file at will.

Suppose you wanted to bring back the Requests library that you removed from the `rp-poetry` project earlier in this tutorial. You can open the `pyproject.toml` file in your text editor and type the necessary declaration in the main group of dependencies:
```toml
[tool.poetry.dependencies]
requests = "*"
```
By using the asterisk (*) as the version constraint, you indicate that you’re not specifying any particular version of the Requests library, and that any version will be acceptable. But this library isn’t installed yet.

### 4.2. Install manually added dependency
If you now open your terminal and navigate to the project’s parent directory, then you can tell Poetry to install the manually added dependencies into the associated virtual environment and update the lock file:
```bash
poetry install
```

> [!CAUTION]
> In this case, Poetry refuses to install the dependencies because your poetry.lock file doesn’t currently mention the Requests library present in the companion pyproject.toml file.
Therefore, to fix such a discrepancy, you could delete the `poetry.lock` file and run poetry install again to let Poetry resolve all dependencies from scratch. That’s not the best approach, though. It’s potentially time-consuming.

> [!TIP]
> A far better approach to align the two files is by manually locking the new dependencies with the poetry lock command:
```bash
poetry lock
```
- This will update your poetry.lock file to match the current pyproject.toml file without installing any dependencies.
- Poetry processes all dependencies in your pyproject.toml file, finds packages that satisfy the declared constraints, and pins their exact versions in the lock file. But Poetry doesn’t stop there. When you run poetry lock, it also recursively traverses and locks all dependencies of your direct dependencies.
- Note: The poetry lock command also updates your existing dependencies if newer versions that still fit your version constraints are available. If you don’t want to update any dependencies that are already in the poetry.lock file, then add the `--no-update` option to the poetry lock command:


### 4.3. Purpose of poetry lock
It’s important to note that dependency locking is only about two things:
- **Resolving**: Finding packages that satisfy all version constraints
- **Pinning**: Taking a snapshot of the resolved versions in the poetry.lock file

Poetry doesn’t actually install the resolved and pinned dependencies for you after running poetry lock. To confirm this, try importing the locked Requests library from the associated virtual environment, which Poetry manages for you:

```bash
poetry run python -c "import requests"
```

When the poetry.lock file agrees with its pyproject.toml counterpart, then you can finally install dependencies that Poetry locked for you:
```bash
poetry install
```
By running poetry install, you make Poetry read the poetry.lock file and install all dependencies listed there. In this case, your virtual environment already had most of the required dependencies in place, so Poetry only installed the missing ones.


## 5. Add poetry to an existing project
Say you have an `rp-hello/` folder with a `hello.py` script inside. But maybe this is just the beginning of a grand project, so you decide to add Poetry to it. Instead of using the poetry new command from before, you’ll use the poetry init command inside your project folder:
```bash
cd rp-hello
poetry init
```
Now, when you show your project’s dependencies as a tree, you’ll know exactly which of them are used by your project directly and which are their transitive dependencies:
```bash
poetry show --tree
```

## 6. Install poetry with pip
There is also an option to install poetry in a projects virtual environment rather than going with `pipx` and then let poetry to utilize that virtual environment for depdency management for you:

Create a virtual environment for your project:
```bash
virtualenv venv
. venv/Script/activate
```

Install poetry in projects virtual environment:
```bash
pip install poetry
which poetry # Validate the poetry installation directory
poetry env info --path # Validate poetry virtual environment
```

Initialize poetry:
```bash
poetry init
```

Install dependencies:
```bash
poetry add fastapi
```


References:
- https://python-poetry.org/docs/
- https://realpython.com/dependency-management-python-poetry/
