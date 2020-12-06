black:
	black advent_of_code_2020/

flake8:
	flake8 advent_of_code_2020/ --statistics

pre-commit: black flake8

setup-day:
	touch advent_of_code_2020/day_$(day).py
	touch advent_of_code_2020/day_$(day)_test.py
	touch inputs/day_$(day)_input.txt
	touch puzzles/day_$(day).md

stage-day:
	git add advent_of_code_2020/day_$(day).py
	git add advent_of_code_2020/day_$(day)_test.py
	git add inputs/day_$(day)_input.txt
	git add puzzles/day_$(day).md
