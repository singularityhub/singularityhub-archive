---
id: 7164
name: "qbicsoftware/rnaseq-power-cli"
branch: "development"
tag: "0.3.2"
commit: "ef88e86fb57154c603470914a70803080c80078e"
version: "0bf87b2a6bc1e7427daf81c8bcdf6009"
build_date: "2019-02-12T21:37:57.888Z"
size_mb: 2216
size: 727576607
sif: "https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.2/2019-02-12-ef88e86f-0bf87b2a/0bf87b2a6bc1e7427daf81c8bcdf6009.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/rnaseq-power-cli/0.3.2/2019-02-12-ef88e86f-0bf87b2a/
recipe: https://datasets.datalad.org/shub/qbicsoftware/rnaseq-power-cli/0.3.2/2019-02-12-ef88e86f-0bf87b2a/Singularity
collection: qbicsoftware/qbic-singularity-rnaseqsamplesize
---

# qbicsoftware/rnaseq-power-cli:0.3.2

```bash
$ singularity pull shub://qbicsoftware/rnaseq-power-cli:0.3.2
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
    environment.yml 
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

