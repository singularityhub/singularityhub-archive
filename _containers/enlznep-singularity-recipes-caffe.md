---
id: 8910
name: "enlznep/singularity-recipes"
branch: "master"
tag: "caffe"
commit: "30be1f59c9809583f698f83a3d45aba0367ddb79"
version: "b23818c427ffb0346f4aadc1c3f5bb28"
build_date: "2019-05-07T14:45:54.332Z"
size_mb: 2393
size: 1007210527
sif: "https://datasets.datalad.org/shub/enlznep/singularity-recipes/caffe/2019-05-07-30be1f59-b23818c4/b23818c427ffb0346f4aadc1c3f5bb28.simg"
url: https://datasets.datalad.org/shub/enlznep/singularity-recipes/caffe/2019-05-07-30be1f59-b23818c4/
recipe: https://datasets.datalad.org/shub/enlznep/singularity-recipes/caffe/2019-05-07-30be1f59-b23818c4/Singularity
collection: enlznep/singularity-recipes
---

# enlznep/singularity-recipes:caffe

```bash
$ singularity pull shub://enlznep/singularity-recipes:caffe
```

## Singularity Recipe

```singularity
BootStrap: shub
From: enlznep/singularity-recipes:opa

%help
    Containerized Intel Caffe and Intel Omni-Path Architecture

%labels
    Maintainer Ray Marc Marcellones
    Version v0.1

%post
    cd /opt
    git clone https://github.com/intel/caffe.git intel-caffe
    cd intel-caffe
    cp Makefile.config.example Makefile.config
    NUM_THREADS=$(($(grep 'core id' /proc/cpuinfo | sort -u | wc -l)*2))
    make -j $NUM_THREADS

%environment
    source /opt/intel-caffe/external/mlsl/l_mlsl_2018.1.005/intel64/bin/mlslvars.sh
    CAFFE_ROOT=/opt/intel-caffe/build/tools/caffe
    export CAFFE_ROOT

%runscript
    exec $CAFFE_ROOT
```

## Collection

 - Name: [enlznep/singularity-recipes](https://github.com/enlznep/singularity-recipes)
 - License: None

