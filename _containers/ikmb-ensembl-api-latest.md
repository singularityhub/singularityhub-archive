---
id: 11007
name: "ikmb/ensembl-api"
branch: "master"
tag: "latest"
commit: "7c7a26864d28f2442ba3dba0724501ac1a3ae7ff"
version: "586a9124fa0a940b0a386c2d6e187fb2"
build_date: "2020-07-15T07:45:54.564Z"
size_mb: 2047.0
size: 1022791711
sif: "https://datasets.datalad.org/shub/ikmb/ensembl-api/latest/2020-07-15-7c7a2686-586a9124/586a9124fa0a940b0a386c2d6e187fb2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ikmb/ensembl-api/latest/2020-07-15-7c7a2686-586a9124/
recipe: https://datasets.datalad.org/shub/ikmb/ensembl-api/latest/2020-07-15-7c7a2686-586a9124/Singularity
collection: ikmb/ensembl-api
---

# ikmb/ensembl-api:latest

```bash
$ singularity pull shub://ikmb/ensembl-api:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:nfcore/base

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the exome-seq pipeline
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/ensembl-api/bin:$PATH
    export PATH
    PERL5LIB /opt/ensembl/99/ensembl/modules:/opt/ensembl/99/ensembl-compara/modules:/opt/ensembl/99/ensembl-variation/modules:/opt/ensembl/99/ensembl-funcgen/modules:$PERL5LIB
    export PERL5LIB
%files
    environment.yml /
    install_api.sh /opt
%post

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

    mkdir -p /ifs
    apt-get -y install procps


    mkdir -p /opt/ensembl/99
    cd /opt/ensembl/99 && bash /opt/install_api.sh 99
```

## Collection

 - Name: [ikmb/ensembl-api](https://github.com/ikmb/ensembl-api)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

