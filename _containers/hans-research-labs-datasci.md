---
id: 7284
name: "hans/research-labs"
branch: "master"
tag: "datasci"
commit: "d09f7d9772f2f85b303eda1cfbd5c582f28892b2"
version: "3b222331fc41cfa2ed27df2bf1ede760"
build_date: "2019-02-18T05:30:07.027Z"
size_mb: 7206
size: 2338701343
sif: "https://datasets.datalad.org/shub/hans/research-labs/datasci/2019-02-18-d09f7d97-3b222331/3b222331fc41cfa2ed27df2bf1ede760.simg"
url: https://datasets.datalad.org/shub/hans/research-labs/datasci/2019-02-18-d09f7d97-3b222331/
recipe: https://datasets.datalad.org/shub/hans/research-labs/datasci/2019-02-18-d09f7d97-3b222331/Singularity
collection: hans/research-labs
---

# hans/research-labs:datasci

```bash
$ singularity pull shub://hans/research-labs:datasci
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: jupyter/datascience-notebook:latest

%environment
	XDG_RUNTIME_DIR=
	HOME=/home/jgauthie

%post
	/opt/conda/bin/conda install --yes simplegeneric r-brms nltk spacy "tensorflow=1.12*" "keras=2.2*"
	/opt/conda/bin/conda clean -tipsy

%runscript
	jupyter lab
```

## Collection

 - Name: [hans/research-labs](https://github.com/hans/research-labs)
 - License: None

