SHELL := /bin/bash

# =============================================================================
# Variables
# =============================================================================

.PHONY: upgrade
upgrade:
	@echo "=> Updating all dependencies"
	@pdm update
	@echo "=> Dependencies updated"

.PHONY: clean
clean:
	@echo "=> Cleaning working directory"
	@rm -fr build/ -fr dist/
	@echo "=> Cleaning working directory"

.PHONY: destroy
destroy:
	@echo "=> Removing .venv dir"
	@rm -fr .venv
	@echo "=> Removal complete"

.PHONY: lock
lock:
	pdm update --update-eager --group :all

# =============================================================================
# Tests, Linting, Coverage
# =============================================================================

.PHONY: coverage
coverage:
	@echo "=> Running tests with coverage"
	@pdm run pytest tests --cov -n auto
	@pdm run coverage html
	@echo "=> Coverage report generated"

.PHONY: test
test:
	@echo "=> Running test cases"
	@pdm run pytest -v tests
	@echo "=> Tests complete"

# =============================================================================
# Build
# =============================================================================

.PHONY: build
build:
	@echo "=> Building wheel"
	@pdm build
	@echo "=> Building complete"
