---
id: 8593
name: "hans/research-labs"
branch: "master"
tag: "deepo-cpu-nlp"
commit: "f263d05ae5eb1d624276fffade50fbd8af3a1a9c"
version: "38b126b1ba4bc82674616190f412f843"
build_date: "2019-10-01T16:04:25.246Z"
size_mb: 3458
size: 927146015
sif: "https://datasets.datalad.org/shub/hans/research-labs/deepo-cpu-nlp/2019-10-01-f263d05a-38b126b1/38b126b1ba4bc82674616190f412f843.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hans/research-labs/deepo-cpu-nlp/2019-10-01-f263d05a-38b126b1/
recipe: https://datasets.datalad.org/shub/hans/research-labs/deepo-cpu-nlp/2019-10-01-f263d05a-38b126b1/Singularity
collection: hans/research-labs
---

# hans/research-labs:deepo-cpu-nlp

```bash
$ singularity pull shub://hans/research-labs:deepo-cpu-nlp
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ufoym/deepo:all-py36-cpu

%environment
	XDG_RUNTIME_DIR=

%post
	pip --no-cache-dir install seaborn statsmodels nltk spacy
	python -m spacy download en
	python -m nltk.downloader punkt
```

## Collection

 - Name: [hans/research-labs](https://github.com/hans/research-labs)
 - License: None

