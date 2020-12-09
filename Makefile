apply-template:
	cp -vn advent_of_code_2020/template_module.py advent_of_code_2020/day_$(day).py
	cp -vn advent_of_code_2020/template_test.py advent_of_code_2020/day_$(day)_test.py

black:
	black advent_of_code_2020/

flake8:
	flake8 advent_of_code_2020/ --statistics

mypy:
	mypy advent_of_code_2020/

pre-commit: black flake8 mypy

setup-day:
	touch advent_of_code_2020/day_$(day).py
	touch advent_of_code_2020/day_$(day)_test.py
	touch inputs/day_$(day)_input.txt
	touch puzzles/day_$(day).md

setup-day-with-template: setup-day apply-template

stage-day:
	git add advent_of_code_2020/day_$(day).py
	git add advent_of_code_2020/day_$(day)_test.py
	git add inputs/day_$(day)_input.txt
	git add puzzles/day_$(day).md
