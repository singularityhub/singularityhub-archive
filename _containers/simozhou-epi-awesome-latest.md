---
id: 8119
name: "simozhou/epi-awesome"
branch: "master"
tag: "latest"
commit: "0d4dcc344631694f18264ec9f8af4bb91f6dbe58"
version: "07c88f8eb085085f94dc6b5b28a27198"
build_date: "2019-04-04T12:23:52.027Z"
size_mb: 1827
size: 687173663
sif: "https://datasets.datalad.org/shub/simozhou/epi-awesome/latest/2019-04-04-0d4dcc34-07c88f8e/07c88f8eb085085f94dc6b5b28a27198.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/simozhou/epi-awesome/latest/2019-04-04-0d4dcc34-07c88f8e/
recipe: https://datasets.datalad.org/shub/simozhou/epi-awesome/latest/2019-04-04-0d4dcc34-07c88f8e/Singularity
collection: simozhou/epi-awesome
---

# simozhou/epi-awesome:latest

```bash
$ singularity pull shub://simozhou/epi-awesome:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Simone Procaccia
    DESCRIPTION Singularity image containing all requirements for the nf-core/epiawesome pipeline
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/nf-core-epiawesome-1.0dev/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [simozhou/epi-awesome](https://github.com/simozhou/epi-awesome)
 - License: [MIT License](https://api.github.com/licenses/mit)

