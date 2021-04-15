# Build the Docs with mkdocs

## Poetry

First you will need to create a python virtual environment. Make sure to install poetry `pip install poetry` and then run inside the `kb` folder:

```bash
cd kb
poetry install
```

## Build your docs

The above will create a python environment for you with your required dependencies to build these docs. Once you have your virtual environment you can test it by serving these docs doing:

```bash
cd on_docs
poetry run mkdocs serve
```

If everything worked correctly you should be able to see the docs site at `http://127.0.0.1:8000`.