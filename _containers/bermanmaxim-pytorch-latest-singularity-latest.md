---
id: 2690
name: "bermanmaxim/pytorch-latest-singularity"
branch: "master"
tag: "latest"
commit: "e0a852ecb96abc8133bc97fa996cbd90803b50da"
version: "702552dcd89ef741c838a3b5b72518c2"
build_date: "2019-11-09T21:49:03.218Z"
size_mb: 5492
size: 2743431199
sif: "https://datasets.datalad.org/shub/bermanmaxim/pytorch-latest-singularity/latest/2019-11-09-e0a852ec-702552dc/702552dcd89ef741c838a3b5b72518c2.simg"
url: https://datasets.datalad.org/shub/bermanmaxim/pytorch-latest-singularity/latest/2019-11-09-e0a852ec-702552dc/
recipe: https://datasets.datalad.org/shub/bermanmaxim/pytorch-latest-singularity/latest/2019-11-09-e0a852ec-702552dc/Singularity
collection: bermanmaxim/pytorch-latest-singularity
---

# bermanmaxim/pytorch-latest-singularity:latest

```bash
$ singularity pull shub://bermanmaxim/pytorch-latest-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: maximdocker/pytorch:latest

%install
  chmod -R o+w /opt/conda
  chmod -R g+w /opt/conda
  chmod -R o+w /opt/pytorch
  chmod -R g+w /opt/pytorch
```

## Collection

 - Name: [bermanmaxim/pytorch-latest-singularity](https://github.com/bermanmaxim/pytorch-latest-singularity)
 - License: None

