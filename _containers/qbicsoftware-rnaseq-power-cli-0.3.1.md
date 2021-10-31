---
id: 6637
name: "qbicsoftware/rnaseq-power-cli"
branch: "development"
tag: "0.3.1"
commit: "824ab10d25e98440d8ca57624c29e21e43647651"
version: "276ddd8269c7f3737e273d85d6ef2d67"
build_date: "2019-02-12T17:08:35.026Z"
size_mb: 1783
size: 611475487
sif: "https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.1/2019-02-12-824ab10d-276ddd82/276ddd8269c7f3737e273d85d6ef2d67.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.1/2019-02-12-824ab10d-276ddd82/
recipe: https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.1/2019-02-12-824ab10d-276ddd82/Singularity
collection: qbicsoftware/qbic-singularity-rnaseqsamplesize
---

# qbicsoftware/rnaseq-power-cli:0.3.1

```bash
$ singularity pull shub://qbicsoftware/rnaseq-power-cli:0.3.1
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Andreas Friedrich <andreas.friedrich@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for the rnaseq samplesize app
    VERSION 0.3.2

%environment
    PATH=/opt/conda/envs/rnaseqsamplesize-1.0/bin:$PATH
    export PATH

%files
    environment.yml /
    script.py /
    sample_size_matrix.R /
    power_matrix.R /
    postman-cli-0.3.0-custom.jar /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

%runscript
    exec python /script.py "$@"
```

## Collection

 - Name: [qbicsoftware/rnaseq-power-cli](https://github.com/qbicsoftware/rnaseq-power-cli)
 - License: [MIT License](https://api.github.com/licenses/mit)

