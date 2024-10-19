
project_dir := .

.PHONY: reformat
reformat:
	@uv run black $(project_dir)
	@uv run ruff check $(project_dir) --fix

.PHONY: lint
lint: reformat
	@uv run mypy $(project_dir)

.PHONY: run
run:
	@uv run python -m app

.PHONY: app-build
app-build:
	@docker compose build

.PHONY: app-run
app-run:
	@docker compose stop
	@docker compose up -d --remove-orphans

.PHONY: app-stop
app-stop:
	@docker compose stop

.PHONY: app-down
app-down:
	@docker compose down

.PHONY: app-destroy
app-destroy:
	@docker compose down -v --remove-orphans

.PHONY: app-logs
app-logs:
	@docker compose logs -f app
