---
id: 5388
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "polish"
commit: "d7ff4615bf12af30eb4f84cdab5c1114ed2e92ac"
version: "b72b9f63930b56118929872b0d52f6ee"
build_date: "2018-11-01T21:55:09.698Z"
size_mb: 2010
size: 833708063
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/polish/2018-11-01-d7ff4615-b72b9f63/b72b9f63930b56118929872b0d52f6ee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/polish/2018-11-01-d7ff4615-b72b9f63/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/polish/2018-11-01-d7ff4615-b72b9f63/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:polish

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:polish
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the tools for assembly polishing and their required
  accessory programs.
  Run `singularity exec polish.simg <tool>`

  Available tools are:
    * Nanopolish
    * Pilon
    * NGM
    * Samtools

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y wget build-essential git zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    #================================
    # INSTALL NANOPOLISH
    #================================
    VERSION="0.9.2"
    git clone --recursive https://github.com/jts/nanopolish.git
    cd nanopolish
    git checkout v"$VERSION"
    make
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
    cd

    #================================
    # INSTALL NGM
    #================================
    VERSION="0.5.5"
    apt install -y cmake
    wget https://github.com/Cibiv/NextGenMap/archive/v"$VERSION".tar.gz -O - | tar xzf -
    cd NextGenMap-"$VERSION"
    mkdir -p build/
    cd build/
    cmake ..
    make
    cd ../bin/ngm*
    chmod 777 ngm
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
    cd

    # ================================
    # INSTALL samtools
    # ================================
    SAMTOOLS_VERSION="1.7"
    SAMTOOLS_URL=https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2
    apt-get install -y libncurses5-dev libbz2-dev liblzma-dev
    wget "$SAMTOOLS_URL" -O - | tar -jxf -
    cd samtools-${SAMTOOLS_VERSION}
    ./configure
    make
    make install
    cd

    # ================================
    # INSTALL pilon
    # ================================
    VERSION="1.22"
    cd /usr/local/bin
    wget -O pilon.jar https://github.com/broadinstitute/pilon/releases/download/v"$VERSION"/pilon-"$VERSION".jar
    # install java
    apt-get install -y debconf-utils
    add-apt-repository -y ppa:webupd8team/java
    apt-get update
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
    apt-get install -y oracle-java8-installer

    echo '#!/usr/bin/env sh\njava -Xmx16G -jar /usr/local/bin/pilon.jar $@' > pilon
    chmod +x pilon
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

