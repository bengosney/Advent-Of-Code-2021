.PHONY := help, clean, test, go
.DEFAULT_GOAL := go

HOOKS=$(.git/hooks/pre-commit)

ALLDAYS=$(wildcard src/day_*.py)
CURRENT_PY=src/day_$(shell date +%d).py
CURRENT_INPUT=inputs/day_$(shell date +%d).txt
COOKIEFILE=cookies.txt

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

requirements.txt: requirements.in
	@echo "Builing $@"
	@pip-compile -q $^

.direnv: .envrc requirements.txt
	pip install --upgrade pip
	pip install wheel pip-tools
	git pull
	pip-sync requirements.txt
	@touch $@ $^

$(COOKIEFILE):
	@echo "$@ not found, add session cookie to $@"
	@false

inputs/day_%.txt: $(COOKIEFILE)
	echo $@
	curl --cookie "$(shell cat $^)" -s -L -o $@ https://adventofcode.com/$(shell date +%Y)/day/$(shell echo "$@" | egrep -o "[0-9]+" | sed 's/^0*//')/input

src/day_%.py:
	cp template.py $@

$(HOOKS):
	pre-commit install

.envrc:
	@echo "Setting up .envrc"
	@echo "layout python python3.10" > $@
	@touch -d '+1 minute' $@
	@false

init: .direnv $(HOOKS) ## Initalise a enviroment

clean:
	find . -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache
	rm -f .testmondata

test: $(ALLDAYS)
	pytest $(ALLDAYS)

go: init $(CURRENT_PY) $(CURRENT_INPUT) ## Setup current day and start runing test monitor
	ptw --runner "pytest --testmon" src/*.py
