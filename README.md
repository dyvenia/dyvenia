# dyvenia
Public dyvenia content

Use https://diataxis.fr/ as a reference

![image](https://user-images.githubusercontent.com/51827647/114751301-44facc00-9d55-11eb-9f31-1d548e2cb774.png)

and [MK Docs](https://squidfunk.github.io/mkdocs-material/) as help for the structure
![image](https://user-images.githubusercontent.com/51827647/114752708-e3d3f800-9d56-11eb-9cb1-dda5db52f4ab.png)


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