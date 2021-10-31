---
id: 3320
name: "khanlab/template-ci"
branch: "master"
tag: "latest"
commit: "0db53123a749f375f1eb3a6c627235706d03c9ec"
version: "e6b60d133734118af13938f8fecabc69"
build_date: "2018-08-03T14:14:03.716Z"
size_mb: 76
size: 27947039
sif: "https://datasets.datalad.org/shub/khanlab/template-ci/latest/2018-08-03-0db53123-e6b60d13/e6b60d133734118af13938f8fecabc69.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/template-ci/latest/2018-08-03-0db53123-e6b60d13/
recipe: https://datasets.datalad.org/shub/khanlab/template-ci/latest/2018-08-03-0db53123-e6b60d13/Singularity
collection: khanlab/template-ci
---

# khanlab/template-ci:latest

```bash
$ singularity pull shub://khanlab/template-ci:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%runscript
    exec echo "Polo $@!"
```

## Collection

 - Name: [khanlab/template-ci](https://github.com/khanlab/template-ci)
 - License: None

