# OpenFisca GovCMS Eligibility

The rules modelled here determine an organisation's eligibility for the
GovCMS program.

- Depending on its organisation type (Australian Government, state or
  territory government, local government, educational institution, developer
  and dev partner, or other), an organisation answers a follow-up question
  about its situation.
- The `govcms_eligible` variable combines these answers into an outcome:
  eligible, eligible with conditions, not eligible, or might be eligible.
- Australian Government bodies can also be matched by name against the
  official list of government bodies.

These elements are described in different folders. All the modelling happens
within the `openfisca_rules` folder.

- The parameters are in the `parameters` folder.
- The formulas are in the `variables` folder.
- The CSV reference data (list of Australian Government bodies) and its
  helpers are in the `csv_data` folder.

The files that are outside from the `openfisca_rules` folder are
used to set up the development environment.

## Install Instructions for Users and Contributors

This package requires
[Python 3.11](https://www.python.org/downloads/release/python-390/). More
recent versions should work, but are not tested.

All platforms that can execute Python are supported, which includes GNU/Linux,
macOS and Microsoft Windows.

The `make` commands used below (e.g. `make test`, `make serve-local`) additionally require [uv](https://docs.astral.sh/uv/).

### Setting-up a Virtual Environment with venv

In order to limit dependencies conflicts, we recommend using a
[virtual environment](https://www.python.org/dev/peps/pep-0405/) with
[venv](https://docs.python.org/3/library/venv.html).

- A [venv](https://docs.python.org/3/library/venv.html) is a project specific
  environment created to suit the needs of the project you are working on.

To create a virtual environment, launch a terminal on your computer, `cd` into
your directory and follow these instructions:

```sh
python3 -m venv .venv # create a new virtual environment in the “.venv” folder, which will contain all dependencies
source .venv/bin/activate # activate the venv
```

You can now operate in the venv you just created.

You can deactivate that venv at any time with `deactivate`.

:tada: You are now ready to install this OpenFisca Country Package!

### A. Installation (Git Clone)

Follow this tutorial if you wish to:

- create or change this Country Package's legislation;
- contribute to the source code.

#### Clone this Country Package with Git

First, make sure [Git](https://www.git-scm.com/) is installed on your machine.

Set your working directory to the location where you want this OpenFisca
Country Package cloned.

Inside your venv, check the prerequisites:

```sh
python --version  # should print "Python 3.11.xx".
```

Clone this Country Package on your machine:

```sh
git clone https://github.com/govCMS/rules-as-code-govcms-eligibility
cd rules-as-code-govcms-eligibility
pip install --upgrade pip build twine
pip install --editable ".[dev]" --upgrade
```

You can make sure that everything is working by running the provided tests with
`make test`.

> [Learn more about tests](https://openfisca.org/doc/coding-the-legislation/writing_yaml_tests.html)

:tada: This OpenFisca Country Package is now installed and ready!

#### Next Steps

- To write new legislation, read the
  [Coding the legislation](https://openfisca.org/doc/coding-the-legislation/index.html)
  section to know how to write legislation.
- To contribute to the code, read our
  [Contribution Guidebook](https://openfisca.org/doc/contribute/index.html).

### B. Contributing

Follow this tutorial if you wish to:

- contribute to the source code.

_Note: This tutorial assumes you have already followed the instructions laid
out in section [A. Installation](#a-installation-git-clone)._

In order to ensure all published versions of this template work as expected,
new contributions are tested in an isolated manner on Github Actions.

Follow these steps to set up an isolated environment for testing your
contributions as Github Actions does.

#### Set up an isolated environment

First, make sur [Tox](https://tox.wiki/en/4.23.0/) is installed on your
machine.

We recommend using [pipx](<(https://pypi.org/project/pipx/)>) to install `tox`,
to avoid mixing isolated-testing dependencies testing with `virtualenv`.

```sh
pipx install tox
```

#### Testing your contribution in an isolated environment

You can make sure that your contributions will work as expected by running:

```sh
tox
```

You can also run these in parallel:

```sh
tox -p
```

:tada: Your contribution to OpenFisca Country Package is now ready for prime
time!

#### Next Steps

- Open a pull request to the `main` branch of this repository.
- Announce your changes as described in [CONTRIBUTING](CONTRIBUTING.md).

## Serve this Country Package with the OpenFisca Web API

If you are considering building a web application, you can use the packaged
OpenFisca Web API with your Country Package.

To serve the Openfisca Web API locally, run:

```sh
openfisca serve --port 5000 --country-package openfisca_rules
```

Or use the quick-start Make command:

```
make serve-local
```

To read more about the `openfisca serve` command, check out its
[documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html).

You can make sure that your instance of the API is working by requesting:

```sh
curl "http://localhost:5000/spec"
```

This endpoint returns the [Open API specification](https://www.openapis.org/)
of your API.

:tada: This OpenFisca Country Package is now served by the OpenFisca Web API!
To learn more, go to the
[OpenFisca Web API documentation](https://openfisca.org/doc/openfisca-web-api/index.html).

You can test your new Web API by sending it example JSON data located in the
`situation_examples` folder.

```sh
curl -X POST -H "Content-Type: application/json" \
  -d @./openfisca_rules/situation_examples/govcms.json \
  http://localhost:5000/calculate
```
