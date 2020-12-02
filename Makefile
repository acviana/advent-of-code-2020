black:
	black advent_of_code_2020/

flake8:
	flake8 advent_of_code_2020/ --statistics

pre-commit: black flake8
