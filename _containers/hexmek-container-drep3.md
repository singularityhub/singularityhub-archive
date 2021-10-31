---
id: 15269
name: "hexmek/container"
branch: "master"
tag: "drep3"
commit: "09a0aca23d1f7638eca03aa20a4603d6afe56b0c"
version: "32902828d465f7e35e195f26dc20f6bf66aed73ee16024d2e193bca6a93e6367"
build_date: "2021-03-09T07:55:30.757Z"
size_mb: 814.046875
size: 853590016
sif: "https://datasets.datalad.org/shub/hexmek/container/drep3/2021-03-09-09a0aca2-32902828/32902828d465f7e35e195f26dc20f6bf66aed73ee16024d2e193bca6a93e6367.sif"
url: https://datasets.datalad.org/shub/hexmek/container/drep3/2021-03-09-09a0aca2-32902828/
recipe: https://datasets.datalad.org/shub/hexmek/container/drep3/2021-03-09-09a0aca2-32902828/Singularity
collection: hexmek/container
---

# hexmek/container:drep3

```bash
$ singularity pull shub://hexmek/container:drep3
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

     conda install -c conda-forge -c bioconda "drep>=3.0" "fastani>=1.32"


%environment
    export LC_ALL=C
```

## Collection

 - Name: [hexmek/container](https://github.com/hexmek/container)
 - License: None

