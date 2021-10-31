---
id: 14490
name: "willgpaik/r_aci"
branch: "master"
tag: "rstan"
commit: "3b6f5ed4b709d44ecd8eafaed630f29155ebe67e"
version: "967d173020e44ccc3495e90d6ff00ca8dd45ab15df3f55312e3618f46723a390"
build_date: "2020-12-12T11:24:45.944Z"
size_mb: 3237.0
size: 1096511488
sif: "https://datasets.datalad.org/shub/willgpaik/r_aci/rstan/2020-12-12-3b6f5ed4-967d1730/967d173020e44ccc3495e90d6ff00ca8dd45ab15df3f55312e3618f46723a390.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/r_aci/rstan/2020-12-12-3b6f5ed4-967d1730/
recipe: https://datasets.datalad.org/shub/willgpaik/r_aci/rstan/2020-12-12-3b6f5ed4-967d1730/Singularity
collection: willgpaik/r_aci
---

# willgpaik/r_aci:rstan

```bash
$ singularity pull shub://willgpaik/r_aci:rstan
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: willgpaik/r_aci:latest

%environment
    source /opt/rh/devtoolset-8/enable
    export PATH=$PATH:/opt/sw/r/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/sw/r/lib64
    
%runscript
    exec "$@"

%post
    yum -y install v8-devel
    yum -y update
    
    source /opt/rh/devtoolset-8/enable

    export PATH=$PATH:/opt/sw/r/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/sw/r/lib64

    R --vanilla -e "install.packages('rstan', repos='http://lib.stat.cmu.edu/R/CRAN/')"
```

## Collection

 - Name: [willgpaik/r_aci](https://github.com/willgpaik/r_aci)
 - License: None

