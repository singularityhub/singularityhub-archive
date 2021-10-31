---
id: 7546
name: "manasi-t24/singularity_recipes"
branch: "master"
tag: "start"
commit: "523aad04b3ad77a320b9dfa436f20714ec324eee"
version: "8df16e081b747eb95298b124a0d2352a"
build_date: "2019-03-01T19:49:13.805Z"
size_mb: 8383
size: 5930442783
sif: "https://datasets.datalad.org/shub/manasi-t24/singularity_recipes/start/2019-03-01-523aad04-8df16e08/8df16e081b747eb95298b124a0d2352a.simg"
url: https://datasets.datalad.org/shub/manasi-t24/singularity_recipes/start/2019-03-01-523aad04-8df16e08/
recipe: https://datasets.datalad.org/shub/manasi-t24/singularity_recipes/start/2019-03-01-523aad04-8df16e08/Singularity
collection: manasi-t24/singularity_recipes
---

# manasi-t24/singularity_recipes:start

```bash
$ singularity pull shub://manasi-t24/singularity_recipes:start
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04



%post
apt-get -y update
apt-get -y install fortune cowsay lolcat
apt-get -y install vim
apt-get -y update
apt-get -y install wget
apt-get -y install cmake
wget "https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64"
dpkg -i cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64
apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
apt-get -y update
apt-get -y install cuda
cd /usr/local/cuda/include/
wget "https://github.com/cusplibrary/cusplibrary/archive/v0.4.0.tar.gz"
tar zxvf *tar.gz
apt-get -y install build-essential flex bison zlib1g-dev qt4-dev-tools libqt4-dev gnuplot libreadline-dev \
libncurses-dev libxt-dev libopenmpi-dev openmpi-bin
apt-get -y update
apt-get -y install binutils-gold

%environment
export LC_ALL=C
export PATH=/usr/games:$PATH
export PATH=$PATH:/usr/local/cuda/bin
```

## Collection

 - Name: [manasi-t24/singularity_recipes](https://github.com/manasi-t24/singularity_recipes)
 - License: None

