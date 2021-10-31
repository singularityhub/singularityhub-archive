---
id: 3785
name: "idot/Singularity_recipes"
branch: "master"
tag: "albacore"
commit: "015ef5873e3dcc628303a5174556421add6b39f9"
version: "58067264b39dd5e557be2c695f58d1e0"
build_date: "2018-07-31T15:32:55.898Z"
size_mb: 832
size: 399999007
sif: "https://datasets.datalad.org/shub/idot/Singularity_recipes/albacore/2018-07-31-015ef587-58067264/58067264b39dd5e557be2c695f58d1e0.simg"
url: https://datasets.datalad.org/shub/idot/Singularity_recipes/albacore/2018-07-31-015ef587-58067264/
recipe: https://datasets.datalad.org/shub/idot/Singularity_recipes/albacore/2018-07-31-015ef587-58067264/Singularity
collection: idot/Singularity_recipes
---

# idot/Singularity_recipes:albacore

```bash
$ singularity pull shub://idot/Singularity_recipes:albacore
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
The Oxford Nanopore basecaller Albacore (version 2.3.1).

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
    VERSION='2.3.1'
    apt-get install -y \
      apt-transport-https python3-pip \
      libboost-filesystem1.58.0 \
      libboost-program-options1.58.0 \
      libboost-python1.58.0 \
      libboost-system1.58.0 \
      libboost-date-time1.58.0 \
      python3-h5py \
      python3-numpy \
      python3-dateutil \
      python3-progressbar \
      libhdf5-cpp-11
    # throws error and is not necessary pip3 install --upgrade setuptools pip
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

 - Name: [idot/Singularity_recipes](https://github.com/idot/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

