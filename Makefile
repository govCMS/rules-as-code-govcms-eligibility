all: test

uninstall:
	uv pip uninstall openfisca-govcms_eligibility || true

clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;
	find . -type d -name '__pycache__' -exec rm -r {} +

deps:
	@# Dependencies are managed via uv sync, but keep this target for compatibility
	uv sync --group dev

install:
	@# Install openfisca-govcms_eligibility for development.
	@# `make install` installs the editable version of openfisca-govcms_eligibility.
	@# This allows contributors to test as they code.
	uv sync --group dev

build: clean
	@# Install openfisca-govcms_eligibility for deployment and publishing.
	@# `make build` allows us to be sure tests are run against the packaged version
	@# of openfisca-govcms_eligibility, the same we put in the hands of users and reusers.
	uv sync --group dev
	uv build
	uv pip uninstall --yes openfisca-govcms_eligibility 2>/dev/null || true
	find dist -name "*.whl" -exec uv pip install --force-reinstall {}[dev] \;

format:
	@# Do not analyse .gitignored files. Ruff format + ruff check --fix (imports, etc.).
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	uv run ruff format `git ls-files | grep "\.py$$"`
	uv run ruff check --fix `git ls-files | grep "\.py$$"`

check-syntax-errors:
	@# Check Python syntax errors.
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	@uv run python -m py_compile `git ls-files | grep "\.py$$"` 2>&1 || (echo "Syntax errors found" && exit 1)

check-style: lint

lint:
	@# Do not analyse .gitignored files.
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	uv run ruff check --exit-zero `git ls-files | grep "\.py$$"`
	uv run ruff format --check `git ls-files | grep "\.py$$"`
	uv run yamllint `git ls-files | grep "\.yaml$$"`

test: clean
	@# Remove stale or duplicate .dist-info so only one version's metadata is visible (avoids AttributeError on get("Name").lower()).
	@rm -rf .venv/lib/python*/site-packages/openfisca_govcms_eligibility-*.dist-info 2>/dev/null || true
	uv sync --group dev
	@# Path must be openfisca_govcms_eligibility/tests only (not the whole package), so parameter YAMLs are not collected as tests.
	uv run openfisca test --country-package openfisca_govcms_eligibility openfisca_govcms_eligibility/tests

# Run the same checks as the CI (validate workflow), without the version/changelog check.
ci: check-syntax-errors check-style
	@bash .github/lint-files.sh "*.py" "uv run ruff check --exit-zero"
	@bash .github/lint-files.sh "openfisca_govcms_eligibility/tests/*.yaml" "uv run yamllint"
	$(MAKE) test

serve-local: build
	uv run openfisca serve --country-package openfisca_govcms_eligibility
