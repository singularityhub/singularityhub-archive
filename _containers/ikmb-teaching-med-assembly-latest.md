---
id: 14987
name: "ikmb/teaching-med-assembly"
branch: "main"
tag: "latest"
commit: "84e93a05017887417da38a5aadb462de57207ef9"
version: "140a2bbcf55244ad047afb62e4c2afe6"
build_date: "2020-11-30T08:27:34.281Z"
size_mb: 3090.0
size: 1092825119
sif: "https://datasets.datalad.org/shub/ikmb/teaching-med-assembly/latest/2020-11-30-84e93a05-140a2bbc/140a2bbcf55244ad047afb62e4c2afe6.sif"
url: https://datasets.datalad.org/shub/ikmb/teaching-med-assembly/latest/2020-11-30-84e93a05-140a2bbc/
recipe: https://datasets.datalad.org/shub/ikmb/teaching-med-assembly/latest/2020-11-30-84e93a05-140a2bbc/Singularity
collection: ikmb/teaching-med-assembly
---

# ikmb/teaching-med-assembly:latest

```bash
$ singularity pull shub://ikmb/teaching-med-assembly:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/miniconda2

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the assembly exercise in the MSc course
    VERSION 2020

%environment
    PATH=/opt/conda/envs/teaching-assembly-2020/bin:/opt/bin:$PATH
    export PATH

%files
    environment.yml /
    FastaStat.pl /

%post

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

    mkdir -p /opt/bin
    mv /FastaStat.pl /opt/bin
    chmod +x /opt/bin/FastaStat.pl
```

## Collection

 - Name: [ikmb/teaching-med-assembly](https://github.com/ikmb/teaching-med-assembly)
 - License: None

