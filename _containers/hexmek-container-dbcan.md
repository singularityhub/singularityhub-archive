---
id: 15710
name: "hexmek/container"
branch: "master"
tag: "dbcan"
commit: "14a17f97b453494dcf6407b91263d2ac187d09b3"
version: "499129e909be14a94bbe61570d84bb480f3476b518a24b94e879eb7e0d31e1aa"
build_date: "2021-03-16T11:16:09.581Z"
size_mb: 614.6015625
size: 644456448
sif: "https://datasets.datalad.org/shub/hexmek/container/dbcan/2021-03-16-14a17f97-499129e9/499129e909be14a94bbe61570d84bb480f3476b518a24b94e879eb7e0d31e1aa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/hexmek/container/dbcan/2021-03-16-14a17f97-499129e9/
recipe: https://datasets.datalad.org/shub/hexmek/container/dbcan/2021-03-16-14a17f97-499129e9/Singularity
collection: hexmek/container
---

# hexmek/container:dbcan

```bash
$ singularity pull shub://hexmek/container:dbcan
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: conda/miniconda3

%post
    apt update
    apt upgrade -y
    apt install -y python3 python3-pip libgl1-mesa-glx rsync git curl wget bwa \
                   bedtools samtools procps parallel


    pip install run-dbcan==2.0.11
    conda install python=3.8 diamond hmmer prodigal -c conda-forge -c bioconda


%environment
    export LC_ALL=C
```

## Collection

 - Name: [hexmek/container](https://github.com/hexmek/container)
 - License: None

