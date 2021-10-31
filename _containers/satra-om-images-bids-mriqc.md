---
id: 420
name: "satra/om-images"
branch: "bids-mriqc"
tag: "bids-mriqc"
commit: "16763d38b5c27a46eb3fcf8ba7443e6d89ea466b"
version: "3565598fd3e3485f17393b6c37caec14"
build_date: "2017-10-19T17:45:42.646Z"
size_mb: 5849
size: 2263293052
sif: "https://datasets.datalad.org/shub/satra/om-images/bids-mriqc/2017-10-19-16763d38-3565598f/3565598fd3e3485f17393b6c37caec14.img.gz"
datalad_url: https://datasets.datalad.org?dir=/shub/satra/om-images/bids-mriqc/2017-10-19-16763d38-3565598f/
recipe: https://datasets.datalad.org/shub/satra/om-images/bids-mriqc/2017-10-19-16763d38-3565598f/Singularity
collection: satra/om-images
---

# satra/om-images:bids-mriqc

```bash
$ singularity pull shub://satra/om-images:bids-mriqc
```

## Singularity Recipe

```singularity
# This container will run mriqc via singularity

BootStrap: docker
From: poldracklab/mriqc:latest

%runscript
    exec /usr/local/miniconda/bin/mriqc "$@"

%setup
    cp -r $SINGULARITY_ROOTFS/root/src $SINGULARITY_ROOTFS/opt
    chmod -R a+r $SINGULARITY_ROOTFS/opt/src

%post
    export PATH=/usr/local/miniconda/bin:$PATH
    pip install /opt/src/mriqc
    echo "
export PATH=/usr/local/miniconda/bin:$PATH
export LANG=C.UTF-8
export LC_ALL=C.UTF-8    

. /etc/fsl/fsl.sh
. /etc/afni/afni.sh
    
" >> /environment

    mkdir /om
    mkdir /cm
```

## Collection

 - Name: [satra/om-images](https://github.com/satra/om-images)
 - License: None

