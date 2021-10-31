---
id: 5173
name: "khanlab/mp2rage_correction"
branch: "master"
tag: "v0.0.3"
commit: "567aaacb6c37e32c2c473a183d3c4dd29913a32e"
version: "3c43e33f3bb2ad5af1e735dbb52e870b"
build_date: "2019-12-08T19:49:41.144Z"
size_mb: 9580
size: 3854798879
sif: "https://datasets.datalad.org/shub/khanlab/mp2rage_correction/v0.0.3/2019-12-08-567aaacb-3c43e33f/3c43e33f3bb2ad5af1e735dbb52e870b.simg"
url: https://datasets.datalad.org/shub/khanlab/mp2rage_correction/v0.0.3/2019-12-08-567aaacb-3c43e33f/
recipe: https://datasets.datalad.org/shub/khanlab/mp2rage_correction/v0.0.3/2019-12-08-567aaacb-3c43e33f/Singularity
collection: khanlab/mp2rage_correction
---

# khanlab/mp2rage_correction:v0.0.3

```bash
$ singularity pull shub://khanlab/mp2rage_correction:v0.0.3
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

