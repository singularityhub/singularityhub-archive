---
id: 1597
name: "khanlab/mp2rage_correction"
branch: "master"
tag: "v0.0.1"
commit: "d0e546274b264f6f9ec29d63ddaa9cf7f81a6ca6"
version: "ffc279ba253055df3a7de6e700124463"
build_date: "2018-02-04T22:11:50.359Z"
size_mb: 9581
size: 3854905375
sif: "https://datasets.datalad.org/shub/khanlab/mp2rage_correction/v0.0.1/2018-02-04-d0e54627-ffc279ba/ffc279ba253055df3a7de6e700124463.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/mp2rage_correction/v0.0.1/2018-02-04-d0e54627-ffc279ba/
recipe: https://datasets.datalad.org/shub/khanlab/mp2rage_correction/v0.0.1/2018-02-04-d0e54627-ffc279ba/Singularity
collection: khanlab/mp2rage_correction
---

# khanlab/mp2rage_correction:v0.0.1

```bash
$ singularity pull shub://khanlab/mp2rage_correction:v0.0.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-core:v1.0.0

#########
%setup
#########
mkdir $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src

#########
%post
#########

cd /src

# checkout specific git release 
#SINGULARITY_TAG=${SINGULARITY_BUILDDEF#Singularity.}
#if [ ! "$SINGULARITY_TAG" = "Singularity" ]
#then
#  git checkout $SINGULARITY_TAG
#fi

#MCR
./install_scripts/05.install_MCR.sh /opt v93 R2017b


#########
%environment

export MCRROOT=/opt/mcr/v93
export PATH=/src/mcr/v93/mp2rage_correction:/src/bin:$PATH

%runscript
exec /src/mp2rage_correction $@
```

## Collection

 - Name: [khanlab/mp2rage_correction](https://github.com/khanlab/mp2rage_correction)
 - License: None

