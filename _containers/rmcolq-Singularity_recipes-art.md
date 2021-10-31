---
id: 6251
name: "rmcolq/Singularity_recipes"
branch: "master"
tag: "art"
commit: "029f6dbf82ea33c9f2f05d534cdd4b174604a82c"
version: "b4f6de694432e94da15eee1bd19649de"
build_date: "2019-01-16T07:21:12.153Z"
size_mb: 1407
size: 634261535
sif: "https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/art/2019-01-16-029f6dbf-b4f6de69/b4f6de694432e94da15eee1bd19649de.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rmcolq/Singularity_recipes/art/2019-01-16-029f6dbf-b4f6de69/
recipe: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/art/2019-01-16-029f6dbf-b4f6de69/Singularity
collection: rmcolq/Singularity_recipes
---

# rmcolq/Singularity_recipes:art

```bash
$ singularity pull shub://rmcolq/Singularity_recipes:art
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the read simulator nanosim.
  Run `singularity exec nanosim.simg nanosim`

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt-get update
    apt-get install -y --no-install-recommends apt-utils
    apt-get update
    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y \
      automake \
      build-essential \
      cmake \
      git \
      gnuplot \
      graphviz \
      openjdk-8-jre \
      libbz2-dev \
      libfreetype6-dev \
      libhts-dev \
      liblzma-dev \
      libncurses5-dev \
      libncursesw5-dev \
      pkg-config \
      python3-dev \
      python3-pip \
      python3-setuptools \
      python3-tk \
      python3-venv \
      samtools \
      tabix \
      vcftools \
      wget \
      zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    
    #============================================
    # INSTALL ART
    #============================================
    wget https://www.niehs.nih.gov/research/resources/assets/docs/artbinmountrainier2016.06.05linux64.tgz
    tar xzf artbinmountrainier2016.06.05linux64.tgz
    echo "export PATH=/art_bin_MountRainier/:$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [rmcolq/Singularity_recipes](https://github.com/rmcolq/Singularity_recipes)
 - License: None

