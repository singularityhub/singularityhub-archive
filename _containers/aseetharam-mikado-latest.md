---
id: 13858
name: "aseetharam/mikado"
branch: "master"
tag: "latest"
commit: "afeb6f104f8ba655eb9fbb290a7e8a9714f563c9"
version: "e967ae3bfaf0ad6e57998063e13f303d"
build_date: "2020-10-25T10:03:18.619Z"
size_mb: 1323.0
size: 396939295
sif: "https://datasets.datalad.org/shub/aseetharam/mikado/latest/2020-10-25-afeb6f10-e967ae3b/e967ae3bfaf0ad6e57998063e13f303d.sif"
url: https://datasets.datalad.org/shub/aseetharam/mikado/latest/2020-10-25-afeb6f10-e967ae3b/
recipe: https://datasets.datalad.org/shub/aseetharam/mikado/latest/2020-10-25-afeb6f10-e967ae3b/Singularity
collection: aseetharam/mikado
---

# aseetharam/mikado:latest

```bash
$ singularity pull shub://aseetharam/mikado:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: conda/miniconda3-centos7

%test
    export PATH="/usr/local/bin:$PATH:/usr/local/conda/bin/"
    python --version
    python -c "import numpy"
    mikado --help

%files
    environment.yml /

%environment
    export PYTHONDONTWRITEBYTECODE=true

%post

    ### Install your packages ###

    export PYTHONDONTWRITEBYTECODE=true
    conda env update --prune -n base -f /environment.yml && conda clean -afy
    yum -y install git wget zlib1g-dev gcc gcc-c++ && yum clean all
    git clone https://github.com/EI-CoreBioinformatics/mikado.git /usr/local/src/mikado
    cd /usr/local/src/mikado
    python3 setup.py bdist_wheel && pip install --prefix /usr/local dist/*whl

    echo '#!/bin/bash' >> /usr/local/bin/show_commit_hash
    chash=$(git log | head -n1 | cut -f 2 -d " ")
    echo -e "echo ${chash}" >> /usr/local/bin/show_commit_hash
    chmod 775 /usr/local/bin/show_commit_hash
    chmod -R 775 /usr/local/src/mikado/util/*
    for TOOL in /usr/local/src/mikado/util/*
    	do
		script=$(basename ${TOOL}) && cp ${TOOL} /usr/local/bin/${script}
        done
    cd /usr/local/src;
    rm -rf mikado;

%apprun snakemake
	snakemake "@"

%apprun mikado
	mikado "@"

%apprun daijin
    daijin "@"

%apprun prodigal
    prodigal "@"

%apprun samtools
    samtools "@"

%apprun diamond
    diamond "@"
```

## Collection

 - Name: [aseetharam/mikado](https://github.com/aseetharam/mikado)
 - License: [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)

