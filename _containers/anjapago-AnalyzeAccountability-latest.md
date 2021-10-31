---
id: 9713
name: "anjapago/AnalyzeAccountability"
branch: "master"
tag: "latest"
commit: "030c5dfe07b157cae96b6a237d2dbb3bea2f7928"
version: "34db2d2421365c6d13ddc79295b1e639"
build_date: "2019-08-20T23:34:12.245Z"
size_mb: 3131.0
size: 1984942111
sif: "https://datasets.datalad.org/shub/anjapago/AnalyzeAccountability/latest/2019-08-20-030c5dfe-34db2d24/34db2d2421365c6d13ddc79295b1e639.sif"
url: https://datasets.datalad.org/shub/anjapago/AnalyzeAccountability/latest/2019-08-20-030c5dfe-34db2d24/
recipe: https://datasets.datalad.org/shub/anjapago/AnalyzeAccountability/latest/2019-08-20-030c5dfe-34db2d24/Singularity
collection: anjapago/AnalyzeAccountability
---

# anjapago/AnalyzeAccountability:latest

```bash
$ singularity pull shub://anjapago/AnalyzeAccountability:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post
    apt-get update && apt-get -y install git wget

    apt-get -y install python3 python3-pip
    apt-get clean

    pip3 install numpy matplotlib scikit-learn
    pip3 install pandas
    pip3 install scipy
    pip3 install scikit-learn
    pip3 install nltk
    pip3 install xlrd
    pip3 install git+https://github.com/anjapago/flair

%environment
  SHELL=/bin/bash
  export SHELL

%runscript
    exec python3 flair_opt.py
```

## Collection

 - Name: [anjapago/AnalyzeAccountability](https://github.com/anjapago/AnalyzeAccountability)
 - License: None

