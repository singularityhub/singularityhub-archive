---
id: 1755
name: "mafreitas/singularity-openms"
branch: "master"
tag: "contrib"
commit: "8c8cf4b0a51a581a892e01ff23bb131685d1a4a2"
version: "6574be6fbc02b22ef9e3f0db75747abb"
build_date: "2020-07-11T09:41:27.555Z"
size_mb: 1466
size: 653410335
sif: "https://datasets.datalad.org/shub/mafreitas/singularity-openms/contrib/2020-07-11-8c8cf4b0-6574be6f/6574be6fbc02b22ef9e3f0db75747abb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mafreitas/singularity-openms/contrib/2020-07-11-8c8cf4b0-6574be6f/
recipe: https://datasets.datalad.org/shub/mafreitas/singularity-openms/contrib/2020-07-11-8c8cf4b0-6574be6f/Singularity
collection: mafreitas/singularity-openms
---

# mafreitas/singularity-openms:contrib

```bash
$ singularity pull shub://mafreitas/singularity-openms:contrib
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mafreitas/singularity-openms:dependencies

%environment
LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH

%post
# build java
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
add-apt-repository -y ppa:webupd8team/java
apt-get -y update
apt-get install -y oracle-java8-installer
apt-get clean
apt-get purge
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# build contrib
cd $HOME
git clone https://github.com/OpenMS/contrib.git
rm -rf contrib/.git/
mkdir contrib-build
cd $HOME/contrib-build

cmake -DBUILD_TYPE=SEQAN ../contrib && rm -rf archives src
cmake -DBUILD_TYPE=WILDMAGIC ../contrib && rm -rf archives src
cmake -DBUILD_TYPE=EIGEN ../contrib && rm -rf archives src
cmake -DBUILD_TYPE=COINOR ../contrib && rm -rf archives src
cmake -DBUILD_TYPE=SQLITE ../contrib && rm -rf archives src
```

## Collection

 - Name: [mafreitas/singularity-openms](https://github.com/mafreitas/singularity-openms)
 - License: None

