---
id: 4235
name: "suujia/botty"
branch: "master"
tag: "latest"
commit: "13a30a397c32148548d00879b4a76fe011b7b4a9"
version: "1532c7be1c37d6b8a760f2090f459f2d"
build_date: "2018-08-29T06:36:16.239Z"
size_mb: 15800
size: 8582725663
sif: "https://datasets.datalad.org/shub/suujia/botty/latest/2018-08-29-13a30a39-1532c7be/1532c7be1c37d6b8a760f2090f459f2d.simg"
url: https://datasets.datalad.org/shub/suujia/botty/latest/2018-08-29-13a30a39-1532c7be/
recipe: https://datasets.datalad.org/shub/suujia/botty/latest/2018-08-29-13a30a39-1532c7be/Singularity
collection: suujia/botty
---

# suujia/botty:latest

```bash
$ singularity pull shub://suujia/botty:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: linuxbrew/linuxbrew

%runscript
	# print out software versions installed by linuxbrew
	find /Software/brew/Cellar -maxdepth 2 -print | sed 's|/Software/brew/Cellar||g' | sed 's|^/||' | grep "/" | sed 's|/|\t|' | sort | awk '{print $1, $2, "Homebrew"}' | column -t | sort -u --ignore-case

%post
    chown -R linuxbrew: /home/linuxbrew/
    chmod 777 /home/linuxbrew/
    chmod 777 /home/linuxbrew/.linuxbrew
    chmod 777 /home/linuxbrew/.linuxbrew/Homebrew

    mkdir /uufs /scratch

    apt-get update \
        && apt-get install -y --no-install-recommends \
                fonts-dejavu-core \
                python-setuptools \
                unzip \
        && rm -rf /var/lib/apt/lists/*
    apt-get clean

    # for brew install to work
    PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH
    echo 'PATH='$PATH >> /etc/environment

    echo "
      export PATH=/usr/local/bin:$PATH
      export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
    " >> /etc/environment

    su -c 'cd /home/linuxbrew/.linuxbrew/Homebrew && git pull' linuxbrew

    # brew can't be run as root, use as linuxbrew user
    su -c 'brew update' linuxbrew
    su -c 'brew tap brewsci/base' linuxbrew
    su -c 'brew tap brewsci/science' linuxbrew
    su -c 'brew tap brewsci/bio' linuxbrew

    su -c 'brew install \
    autoconf \
    automake \
    berkeley-db \
    cpanm \
    expat \
    less \
    libxml2 \
    macse \
    matplotlib \
    miller \
    numpy \
    pandoc \
    python \
    scipy \
    tcsh \
    vim \
    zip \
    zlib' linuxbrew

    pip2 install \
    --upgrade setuptools \
    -U pip \
    biopython

    pip3 install \
    --upgrade setuptools \
    -U pip \
    --no-cache-dir biopython \
    cwlref-runner \
    pandas \
    pyvcf \
    virtualenv

    su -c 'brew install ruby' linuxbrew
    export PATH=/usr/local/lib/ruby/gems/2.0.0/bin:$PATH
    export PATH=/usr/local/opt/ruby20/bin:$PATH
    su -c 'gem install \
    gnuplot \
    narray \
    RubyInline \
    terminal-table \
    && gem cleanup all' linuxbrew

    su -c 'brew install \
    abricate \
    gepard \
    gfalint \
    gfakluge \
    gingr \
    glimmerhmm \
    gmap-gsnap \
    grabix \
    graphviz \
    gsl \
    gzstream \
    harfbuzz \
    hisat \
    hisat2 \
    hlaminer \
    hmmer \
    hmmer2 \
    htsbox \
    htslib \
    humann2 \
    idba \
    igv \
    igvtools \
    impute2 \
    infernal \
    iqtree \
    ispcr \
    jellyfish \
    jpeg \
    jspecies \
    k8 \
    kaiju \
    kallisto \
    kat \
    kent-tools \
    kma \
    kmacs \
    kmc \
    kmergenie \
    kmerstream \
    kollector \
    kr \
    kraken \
    last \
    lastz \
    libbigwig \
    libpll \
    libsequence \
    libtool \
    light-assembler \
    lighter \
    links-scaffolder \
    lofreq \
    lrsim \
    lsd \
    lua \
    lumpy-sv \
    mafft \
    magic-blast \
    makedepend \
    maker \
    linuxbrew/extra/man-db \
    mapsembler2 \
    maq \
    mash \
    mcl \
    megahit \
    meme \
    metaphlan \
    methpipe \
    mhap \
    minced \
    minia \
    miniasm \
    minimap \
    minimap2 \
    mir-prefer \
    mitofy \
    mlst \
    mosdepth \
    mothur \
    mp-est \
    mrbayes \
    multi-worm-tracker \
    mummer \
    muscle \
    nano \
    ncl' linuxbrew
    
    su -c 'brew install perl' linuxbrew
    PERL5LIB=/home/linuxbrew/perl5/lib/perl5
    echo 'PERL5LIB='$PERL5LIB >> /etc/environment
```

## Collection

 - Name: [suujia/botty](https://github.com/suujia/botty)
 - License: None

