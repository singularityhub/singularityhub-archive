---
id: 5658
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "krakenuniq"
commit: "d76b3062b0eb29334c26e9e614e708c6cedf27d7"
version: "c9cacb07202e873d68f324837c8baa01"
build_date: "2019-01-09T15:39:53.455Z"
size_mb: 760
size: 260857887
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/krakenuniq/2019-01-09-d76b3062-c9cacb07/c9cacb07202e873d68f324837c8baa01.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/krakenuniq/2019-01-09-d76b3062-c9cacb07/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/krakenuniq/2019-01-09-d76b3062-c9cacb07/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:krakenuniq

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:krakenuniq
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo "export PATH=/usr/local:/usr/local/bin:$PATH" >> $SINGULARITY_ENVIRONMENT

    # ================================
    # INSTALL blast tools (dustmasker req. for kraken)
    # ================================
    apt install -y libidn11-dev
    VERSION="2.7.1"
    URL=ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/"$VERSION"/ncbi-blast-"$VERSION"+-x64-linux.tar.gz
    wget -O - "$URL" | tar xzf -
    cp ncbi*/bin/dustmasker /usr/local/bin/
    rm -rf ncbi-blast*
    cd ~

    # ================================
    # INSTALL jellyfish
    # ================================
    VERSION="1.1.11"
    URL=http://www.cbcb.umd.edu/software/jellyfish/jellyfish-"$VERSION".tar.gz
    wget -O - "$URL" | tar xzf -
    cd jellyfish*
    ./configure --prefix=/usr/local/
    make
    make install

    # ================================
    # INSTALL krakenuniq
    # ================================
    VERSION="0.5.7"
    URL=https://github.com/fbreitwieser/krakenuniq/archive/v"$VERSION".tar.gz
    apt install -y zlib1g-dev
    wget -O - "$URL" | tar xzf -
    cd krakenuniq-"$VERSION"
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
    ./install_krakenuniq.sh -j $(pwd)
    cd ~
    perl -MCPAN -e'install "LWP::Simple"'
    ln -s /krakenuniq-"$VERSION"/krakenuniq /krakenuniq-"$VERSION"/krakenuniq-build /krakenuniq-"$VERSION"/krakenuniq-download /krakenuniq-"$VERSION"/krakenuniq-extract-reads /krakenuniq-"$VERSION"/krakenuniq-filter /krakenuniq-"$VERSION"/krakenuniq-mpa-report /krakenuniq-"$VERSION"/krakenuniq-report /krakenuniq-"$VERSION"/krakenuniq-translate /usr/local/bin/
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

