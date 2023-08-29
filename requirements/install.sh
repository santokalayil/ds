
curl https://pyenv.run | bash
# curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash # above link comes here first to install

pyenv update

# poetry env use 3.12.0rc1 # this for poetry to use this env



# install polars since issues iwth poetry install
python -m pip install polars
# install ipykernal if not working directly using `poetry add ipykernal --group dev`
python -m pip install ipykernel -U --force-reinstall

# fixing issues with pandas profiling install using poetry
python -m pip install  ydata-profiling  # pandas-profiling # ydata-profiling

 python -m pip install ipywidgets


