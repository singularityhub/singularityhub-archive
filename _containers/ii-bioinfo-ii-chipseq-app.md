---
id: 5580
name: "ii-bioinfo/ii-chipseq"
branch: "master"
tag: "app"
commit: "acf2f9bcd31802923c18c7f95064653c6c22e234"
version: "ab5f2c3857c746c3825a0bca7920b41f"
build_date: "2018-11-19T08:23:52.047Z"
size_mb: 5992
size: 1927344159
sif: "https://datasets.datalad.org/shub/ii-bioinfo/ii-chipseq/app/2018-11-19-acf2f9bc-ab5f2c38/ab5f2c3857c746c3825a0bca7920b41f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ii-bioinfo/ii-chipseq/app/2018-11-19-acf2f9bc-ab5f2c38/
recipe: https://datasets.datalad.org/shub/ii-bioinfo/ii-chipseq/app/2018-11-19-acf2f9bc-ab5f2c38/Singularity
collection: ii-bioinfo/ii-chipseq
---

# ii-bioinfo/ii-chipseq:app

```bash
$ singularity pull shub://ii-bioinfo/ii-chipseq:app
```

## Singularity Recipe

```singularity
From:continuumio/miniconda:4.5.4
Bootstrap:docker

%labels
    MAINTAINER Lukas Lueftinger <lukas.lueftinger@imp.ac.at>
    DESCRIPTION Container image containing all binary dependencies for the ii-chipseq pipeline
    VERSION 0.1dev


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

