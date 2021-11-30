.PHONY := install, help, init, pre-init, postgres, clean, test
.DEFAULT_GOAL := go

HOOKS=$(.git/hooks/pre-commit)
PGCONTAINER:=stl-postgres

ALLDAYS=$(wildcard src/day_*.py)
DAY=src/day_$(shell date +%d).py
INPUT=inputs/day_$(shell date +%d).txt

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

requirements.txt: requirements.in
	@echo "Builing $@"
	@pip-compile -q $^

.direnv: .envrc requirements.txt
	@git pull
	@pip-sync requirements.txt
	@touch $@

$(INPUT):
	touch $@

$(DAY):
	cp template.py $@

$(HOOKS):
	pre-commit install

.envrc:
	@echo "layout python python3.10" > $@
	@touch $@
	@exit 0

pre-init:
	pip install --upgrade pip
	pip install wheel pip-tools

init: .envrc pre-init .direnv $(HOOKS) ## Initalise a enviroment
	git pull
	@echo "Read to dev"

clean:
	find . -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache
	$(init)

test: $(ALLDAYS)
	pytest $(ALLDAYS)

go: init $(DAY) $(INPUT)
	ptw --runner "pytest --testmon" src/*.py
