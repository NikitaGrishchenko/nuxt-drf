# Including commands
run-django-server:
	poetry run task server localhost:8000

run-webpack-server:
	yarn dev

open-localhost:
	python -m webbrowser "http://localhost:3000"

install-backend:
	poetry install

install-frontend:
	yarn

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

.PHONY: createapp $(name)
createapp:
	poetry run task createapp $(name)

# Primary commands
.PHONY: install
install:
	@make -j 2 install-backend install-frontend
	@make migrate
	poetry run task defaultadmin

.PHONY: run
run:
	@make -j 3 run-django-server run-webpack-server open-localhost

.PHONY: build
build:
	yarn build
	poetry run task collectstatic
	@make migrate
