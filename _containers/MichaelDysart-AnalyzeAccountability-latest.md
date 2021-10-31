---
id: 10657
name: "MichaelDysart/AnalyzeAccountability"
branch: "master"
tag: "latest"
commit: "2c6fde4ef896fca909318861d5ea25f411743328"
version: "1385f9bd5bbc285e15efcbd7748ff72e"
build_date: "2019-08-19T04:27:23.425Z"
size_mb: 2506.0
size: 1138667551
sif: "https://datasets.datalad.org/shub/MichaelDysart/AnalyzeAccountability/latest/2019-08-19-2c6fde4e-1385f9bd/1385f9bd5bbc285e15efcbd7748ff72e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MichaelDysart/AnalyzeAccountability/latest/2019-08-19-2c6fde4e-1385f9bd/
recipe: https://datasets.datalad.org/shub/MichaelDysart/AnalyzeAccountability/latest/2019-08-19-2c6fde4e-1385f9bd/Singularity
collection: MichaelDysart/AnalyzeAccountability
---

# MichaelDysart/AnalyzeAccountability:latest

```bash
$ singularity pull shub://MichaelDysart/AnalyzeAccountability:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%post
    apt-get update && apt-get -y install git wget
    /opt/conda/bin/conda install numpy matplotlib scikit-learn
    /opt/conda/bin/pip install pandas
    /opt/conda/bin/pip install scipy
    /opt/conda/bin/pip install scikit-learn
    /opt/conda/bin/pip install nltk
    /opt/conda/bin/pip install xlrd

%environment
  PATH=/opt/conda/bin:$PATH
  export PATH

%runscript
    exec python AnalyzeAccountability/simple_classifier.py
```

## Collection

 - Name: [MichaelDysart/AnalyzeAccountability](https://github.com/MichaelDysart/AnalyzeAccountability)
 - License: None

