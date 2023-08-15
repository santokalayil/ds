poetry export -f requirements.txt --output requirements/requirements.txt --without-hashes
poetry export --with dev -f requirements.txt --output requirements/requirements-dev.txt --without-hashes

sed -i 's/;.*//' requirements/requirements-dev.txt
# grep -E '^(autopep8|flake8|ipykernel)==.*' requirements/requirements-dev.txt > requirements/filtered-requirements-dev.txt
sed -i 's/;.*//' requirements/requirements.txt


