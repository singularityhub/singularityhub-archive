---
id: 2346
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "albacore"
commit: "cba73bf05ddb324464820448e8ce4e9c48d093fa"
version: "4289f9965dd83b7b7bc3baeda7793e52"
build_date: "2018-03-29T17:52:12.098Z"
size_mb: 818
size: 398774303
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/albacore/2018-03-29-cba73bf0-4289f996/4289f9965dd83b7b7bc3baeda7793e52.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/albacore/2018-03-29-cba73bf0-4289f996/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/albacore/2018-03-29-cba73bf0-4289f996/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:albacore

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:albacore
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

# ===================
# GLOBAL
# ===================

%help
The Oxford Nanopore basecaller Albacore (version 2.1.7).

Examples of how to run:
  To get the help menu:
    singularity exec --app albacore basecallers.simg read_fast5_basecaller.py -h
  To list all available protocols and config files:
    sudo singularity exec --app albacore basecallers.simg read_fst5_basecaller.py -l
  To basecall something:
    sudo singularity exec --app albacore basecallers.simg read_fast5_basecaller.py -i /input/dir/ -t num_threads -s /save/to/ -c config_file.cfg

Effectively you can run whatever combination of arguments you can see from the help command listed above.


%post
    apt-get update
    apt-get install -y software-properties-common wget
    apt-add-repository universe
    apt-get update

    # ===================
    # INSTALL ALBACORE
    # ===================
    VERSION='2.1.7'
    apt-get install -y \
      apt-transport-https python3-pip \
      libboost-filesystem1.58.0 \
      libboost-program-options1.58.0 \
      libboost-python1.58.0 \
      libboost-system1.58.0 \
      python3-h5py \
      python3-numpy \
      python3-dateutil \
      python3-progressbar \
      libhdf5-cpp-11
    pip3 install ont-fast5-api
    wget https://mirror.oxfordnanoportal.com/software/analysis/python3-ont-albacore_"$VERSION"-1~xenial_amd64.deb
    apt-get update
    wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | apt-key add -
    echo "deb http://mirror.oxfordnanoportal.com/apt trusty-stable non-free" | tee /etc/apt/sources.list.d/nanoporetech.sources.list
    apt-get update
    apt-get install -y python3-ont-fast5-api
    dpkg -i python3-ont-albacore_"$VERSION"-1~xenial_amd64.deb
    apt-get -yf install
    wget https://mirror.oxfordnanoportal.com/software/analysis/ont_albacore-"$VERSION"-cp35-cp35m-manylinux1_x86_64.whl
    pip3 install ont_albacore-"$VERSION"-cp35-cp35m-manylinux1_x86_64.whl
    rm -rf ont_albacore-"$VERSION"-cp35-cp35m-manylinux1_x86_64.whl
    rm -rf python3-ont-albacore_"$VERSION"-1~xenial_amd64.deb
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

