---
id: 6281
name: "qbicsoftware/rnaseq-power-cli"
branch: "development"
tag: "0.3.0"
commit: "1fa53a76e770ae12d4c7c82482a44eb1e8f74cc7"
version: "d1b7008abf071644d3bd1e7190373862"
build_date: "2019-07-02T23:19:19.133Z"
size_mb: 1879
size: 638468127
sif: "https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.0/2019-07-02-1fa53a76-d1b7008a/d1b7008abf071644d3bd1e7190373862.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.0/2019-07-02-1fa53a76-d1b7008a/
recipe: https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.0/2019-07-02-1fa53a76-d1b7008a/Singularity
collection: qbicsoftware/qbic-singularity-rnaseqsamplesize
---

# qbicsoftware/rnaseq-power-cli:0.3.0

```bash
$ singularity pull shub://qbicsoftware/rnaseq-power-cli:0.3.0
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Andreas Friedrich <andreas.friedrich@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for the rnaseq samplesize app
    VERSION 0.3.0

%environment
    PATH=/opt/conda/envs/rnaseqsamplesize-1.0/bin:$PATH
    export PATH

%files
    environment.yml /
    script.py /
    sample_size_matrix.R /
    power_matrix.R /
    postman-cli-0.3.0.jar /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

%runscript
    exec python /script.py "$@"
```

## Collection

 - Name: [qbicsoftware/rnaseq-power-cli](https://github.com/qbicsoftware/rnaseq-power-cli)
 - License: [MIT License](https://api.github.com/licenses/mit)

