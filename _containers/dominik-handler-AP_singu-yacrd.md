---
id: 10122
name: "dominik-handler/AP_singu"
branch: "master"
tag: "yacrd"
commit: "2a2f559fe0bdd7c6bfe8017f27bfe691aac58636"
version: "745d177706445fefd37c1d00d49468f18e065c5e7a71e1e88ea353331bc63f01"
build_date: "2021-02-01T07:12:07.113Z"
size_mb: 291.48828125
size: 305647616
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/yacrd/2021-02-01-2a2f559f-745d1777/745d177706445fefd37c1d00d49468f18e065c5e7a71e1e88ea353331bc63f01.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/yacrd/2021-02-01-2a2f559f-745d1777/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/yacrd/2021-02-01-2a2f559f-745d1777/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:yacrd

```bash
$ singularity pull shub://dominik-handler/AP_singu:yacrd
```

## Singularity Recipe

```singularity
#bedtools in singularity

Bootstrap: docker
From: conda/miniconda3

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  yacrd from GIT 2019-07-01  

%runscript
    yacrd "$@"

%post
  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels bioconda

  conda install yacrd

%environment


%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

