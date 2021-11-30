.PHONY := install, install-dev, help, init, pre-init, postgres, clean
.DEFAULT_GOAL := install

HOOKS=$(.git/hooks/pre-commit)
PGCONTAINER:=stl-postgres

DAYS=$(wildcard src/day_*.py)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

requirements.txt: requirements.in
	@echo "Builing $@"
	@pip-compile -q $^

install: requirements.txt ## Install requirements
	@git pull
	@echo "Installing $^"
	@pip-sync $^

$(HOOKS):
	pre-commit install

.envrc:
	@echo "layout python python3.10" > $@

pre-init:
	pip install --upgrade pip
	pip install wheel pip-tools

init: .envrc pre-init $(HOOKS) ## Initalise a enviroment
	git pull
	@echo "Read to dev"

clean:
	@echo "Stopping any excisting postgres containers"
	@docker stop $(PGCONTAINER) || true
	@docker rm $(PGCONTAINER) || true

test: $(DAYS)
	pytest $(DAYS)
