black:
	black advent_of_code_2020/

flake8:
	flake8 advent_of_code_2020/ --statistics

pre-commit: black flake8

setup-day:
	touch advent_of_code_2020/day_$(day).py
	touch inputs/day_$(day)_input.txt
	touch puzzles/day_$(day).md
