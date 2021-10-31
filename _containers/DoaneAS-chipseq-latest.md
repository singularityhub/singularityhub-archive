---
id: 6083
name: "DoaneAS/chipseq"
branch: "master"
tag: "latest"
commit: "520cef50801bc953487691624e768cee1ca27029"
version: "1926e5587ee2fe96ff250aea199cca0f"
build_date: "2019-01-08T20:58:21.603Z"
size_mb: 5859
size: 2743910431
sif: "https://datasets.datalad.org/shub/DoaneAS/chipseq/latest/2019-01-08-520cef50-1926e558/1926e5587ee2fe96ff250aea199cca0f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DoaneAS/chipseq/latest/2019-01-08-520cef50-1926e558/
recipe: https://datasets.datalad.org/shub/DoaneAS/chipseq/latest/2019-01-08-520cef50-1926e558/Singularity
collection: DoaneAS/chipseq
---

# DoaneAS/chipseq:latest

```bash
$ singularity pull shub://DoaneAS/chipseq:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Alexander Peltzer <alexander.peltzer@qbic.uni-tuebingen.de>
    DESCRIPTION Container image containing all requirements for the nf-core/chipseq pipeline
    VERSION 1.0dev
    
%environment
    PATH=/opt/conda/envs/nfcore-chipseq-1.4dev/bin:$PATH
    export PATH
    
%files
    environment.yml /

%post
    git clone https://github.com/nf-core/chipseq.git
    /opt/conda/bin/conda env create -f chipseq/environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [DoaneAS/chipseq](https://github.com/DoaneAS/chipseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

