---
id: 14933
name: "frankier/skelshop"
branch: "master"
tag: "latest"
commit: "ddb6043f50f3bd9c9c2994ff080529369b8f01cf"
version: "12354c453c20e5d68af23bc1fe952d10a000e5682e6a7b075f5a01397fb3a4bc"
build_date: "2021-02-01T08:45:20.798Z"
size_mb: 5445.37890625
size: 5709893632
sif: "https://datasets.datalad.org/shub/frankier/skelshop/latest/2021-02-01-ddb6043f-12354c45/12354c453c20e5d68af23bc1fe952d10a000e5682e6a7b075f5a01397fb3a4bc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/frankier/skelshop/latest/2021-02-01-ddb6043f-12354c45/
recipe: https://datasets.datalad.org/shub/frankier/skelshop/latest/2021-02-01-ddb6043f-12354c45/Singularity
collection: frankier/skelshop
---

# frankier/skelshop:latest

```bash
$ singularity pull shub://frankier/skelshop:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: frankierr/skelshop:focal_nvcaffe

%post
    echo "Nothing to do"

%runscript
    cd /opt/skelshop && snakemake "$@"

%environment
    . /.skelshop_env
```

## Collection

 - Name: [frankier/skelshop](https://github.com/frankier/skelshop)
 - License: None

