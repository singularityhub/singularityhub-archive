---
id: 6141
name: "ii-bioinfo/ii-chipseq"
branch: "dev"
tag: "0.2dev"
commit: "bc858a5bbf1dd39a027aec25baba1035fdfd42c3"
version: "698513c81929c67559fc50890d55de91"
build_date: "2019-01-07T17:57:02.774Z"
size_mb: 5539
size: 1923305503
sif: "https://datasets.datalad.org/shub/ii-bioinfo/ii-chipseq/0.2dev/2019-01-07-bc858a5b-698513c8/698513c81929c67559fc50890d55de91.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ii-bioinfo/ii-chipseq/0.2dev/2019-01-07-bc858a5b-698513c8/
recipe: https://datasets.datalad.org/shub/ii-bioinfo/ii-chipseq/0.2dev/2019-01-07-bc858a5b-698513c8/Singularity
collection: ii-bioinfo/ii-chipseq
---

# ii-bioinfo/ii-chipseq:0.2dev

```bash
$ singularity pull shub://ii-bioinfo/ii-chipseq:0.2dev
```

## Singularity Recipe

```singularity
From:continuumio/miniconda:4.5.4
Bootstrap:docker

%labels
    MAINTAINER IMP/IMBA Bioinformatics and Lukas Lueftinger <lukas.lueftinger@imp.ac.at>
    DESCRIPTION Container image containing all binary dependencies for the ii-chipseq pipeline
    VERSION 0.2dev


##############################
# py2
##############################

%appenv py2
    PATH=/opt/conda/envs/ii-bioinfo-py2/bin:$PATH
    export PATH

%appfiles py2
    environment_py2.yaml /

%appinstall py2
    apt-get install -y ttf-liberation procps
    /opt/conda/bin/conda env create -f /scif/apps/py2/environment_py2.yaml
    /opt/conda/bin/conda clean -a

##############################
# py3
##############################

%appenv py3
    PATH=/opt/conda/envs/ii-bioinfo-py3/bin:$PATH
    export PATH

%appfiles py3
    environment_py3.yaml /

%appinstall py3
    apt-get install -y procps
    /opt/conda/bin/conda env create -f /scif/apps/py3/environment_py3.yaml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [ii-bioinfo/ii-chipseq](https://github.com/ii-bioinfo/ii-chipseq)
 - License: None

