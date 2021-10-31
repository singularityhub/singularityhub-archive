---
id: 12383
name: "TomHarrop/funannotate-singularity"
branch: "master"
tag: "funannotate-deps_8e2e0a1"
commit: "43c65857208a36b9c93edd447e6a1d9eaab26445"
version: "ec22457175c487d0588cfbd494c83b06043459dc18ddbbedc83730d678f6f0f5"
build_date: "2020-02-26T02:17:45.899Z"
size_mb: 2653.3515625
size: 2782240768
sif: "https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate-deps_8e2e0a1/2020-02-26-43c65857-ec224571/ec22457175c487d0588cfbd494c83b06043459dc18ddbbedc83730d678f6f0f5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/funannotate-singularity/funannotate-deps_8e2e0a1/2020-02-26-43c65857-ec224571/
recipe: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate-deps_8e2e0a1/2020-02-26-43c65857-ec224571/Singularity
collection: TomHarrop/funannotate-singularity
---

# TomHarrop/funannotate-singularity:funannotate-deps_8e2e0a1

```bash
$ singularity pull shub://TomHarrop/funannotate-singularity:funannotate-deps_8e2e0a1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/funannotate-singularity:funannotate-base_8e2e0a1

# Bootstrap: localimage
# From: funannotate-base_8e2e0a1.sif

%post
    # install augustus
    (
    wget -O "augustus.tar.gz" \
        --no-check-certificate \
        https://github.com/Gaius-Augustus/Augustus/releases/download/v3.3.3/augustus-3.3.3.tar.gz
    mkdir /augustus
    tar -zxf augustus.tar.gz \
        -C /augustus \
        --strip-components 1
    rm -f augustus.tar.gz
    cd /augustus || exit 1

    export CC="$(which gcc)"
    export CXX="$(which g++)"
    export PREFIX="/usr/local"
    export BUILD_PREFIX="/usr"
    export TOOLDIR="/usr/include"

    # follow the conda install recipe
    export INCLUDE_PATH="${PREFIX}/include"
    export LIBRARY_PATH="${PREFIX}/lib"
    export LD_LIBRARY_PATH="${PREFIX}/lib"
    export BOOST_INCLUDE_DIR="${PREFIX}/include"
    export BOOST_LIBRARY_DIR="${PREFIX}/lib"

    export CXXFLAGS=" -std=c++11  -DUSE_BOOST -I${BOOST_INCLUDE_DIR} -L${BOOST_LIBRARY_DIR} -I${BUILD_PREFIX}/include/bamtools"
    export LDFLAGS="-L${BOOST_LIBRARY_DIR}"
    export BAMTOOLS="${BUILD_PREFIX}"

    # compile
    ln -s /usr/lib/libbam.a "${TOOLDIR}/samtools/"
    ln -s /usr/lib/x86_64-linux-gnu/libhts.a "${TOOLDIR}/htslib/"
    make  \
        COMPGENPRED=true \
        SQLITE=true \
        BAMTOOLS="${BUILD_PREFIX}" \
        BAMTOOLS_CC="${CC}" \
        BAMTOOLS_CXX="${CXX}"
    make install
    )

    # augustus config
    export AUGUSTUS_CONFIG_PATH="/opt/augustus-3.3.3/config"
    # allow BUSCO to *write* to the augustus config dir
    chmod -R 777 "${AUGUSTUS_CONFIG_PATH}"

    # install blast 2.2.31 for BUSCO
    wget -O "blast.tar.gz" \
        ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/ncbi-blast-2.2.31+-x64-linux.tar.gz
    mkdir /blast
    tar -zxf blast.tar.gz \
        -C /blast \
        --strip-components 1
    rm -f blast.tar.gz

    # codingquarry
    wget -O "codingquarry.tar.gz" \
        https://sourceforge.net/projects/codingquarry/files/CodingQuarry_v2.0.tar.gz
    mkdir codingquarry
    tar -zxf codingquarry.tar.gz \
        -C codingquarry \
        --strip-components 1
    cd codingquarry || exit 1
    make
    mv CodingQuarry /usr/local/bin/
    cd .. || exit 1
    rm -rf codingquarry codingquarry.tar.gz

    # blat & pslCDnaFilter
    wget -O /usr/local/bin/blat \
        http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/blat
    wget -O /usr/local/bin/pslCDnaFilter \
        http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/pslCDnaFilter

    chmod 755 /usr/local/bin/blat
    chmod 755 /usr/local/bin/pslCDnaFilter

    # pasa
    wget -O "fasta.tar.gz" \
        http://faculty.virginia.edu/wrpearson/fasta/fasta36/fasta-36.3.8g.tar.gz
    mkdir /fasta
    tar -zxf fasta.tar.gz \
        -C /fasta \
        --strip-components 2
    rm -f fasta.tar.gz
    cd /fasta/src || exit 1
    make -f ../make/Makefile.linux_sse2 all
    cd ../.. || exit 1
    cp fasta/bin/fasta36 /usr/local/bin/fasta

    wget -O "pasa.tar.gz" \
        https://github.com/PASApipeline/PASApipeline/releases/download/pasa-v2.3.3/PASApipeline-v2.3.3.tar.gz
    mkdir /pasa
    tar -zxf pasa.tar.gz \
        -C /pasa \
        --strip-components 1
    rm -f pasa.tar.gz
    cd /pasa || exit 1
    make
    cd .. || exit 1

    # genemark
    wget -O /genemark_download.sh \
        --no-check-certificate \
        https://raw.githubusercontent.com/TomHarrop/funannotate-singularity/master/src/genemark_download.sh
    cd / && bash genemark_download.sh || exit 1
    rm /genemark_download.sh

    # kallisto
    wget -O "kallisto.tar.gz" \
        https://github.com/pachterlab/kallisto/releases/download/v0.46.0/kallisto_linux-v0.46.0.tar.gz
    mkdir kallisto
    tar -zxf kallisto.tar.gz \
        -C kallisto \
        --strip-components 1
    mv kallisto/kallisto /usr/local/bin/
    rm -rf kallisto kallisto.tar.gz
 
    # stringtie
    wget -O stringtie.tar.gz \
        --no-check-certificate \
        http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.3.6.Linux_x86_64.tar.gz
    mkdir stringtie

    tar -zxf stringtie.tar.gz \
        -C stringtie \
        --strip-components 1
    mv stringtie/stringtie /usr/local/bin/
    rm -rf stringtie stringtie.tar.gz

    # trimal
    wget -O trimal.tar.gz \
        --no-check-certificate \
        https://github.com/scapella/trimal/archive/v1.4.1.tar.gz
    mkdir trimal
    tar -zxf trimal.tar.gz \
        -C trimal \
        --strip-components 1
    cd trimal/source || exit 1
    make
    mv readal statal trimal /usr/local/bin/
    cd ../../ || exit 1
    rm -rf trimal trimal.tar.gz

    # evidence modeller
    wget -O evm.tar.gz \
        --no-check-certificate \
    https://github.com/EVidenceModeler/EVidenceModeler/archive/v1.1.1.tar.gz
    mkdir /evm
    tar -zxf evm.tar.gz \
        -C /evm \
        --strip-components 1
    rm -f evm.tar.gz

    # trnascan-se \ move to deps?
    wget -O trnascan.tar.gz \
        --no-check-certificate \
        http://trna.ucsc.edu/software/trnascan-se-2.0.5.tar.gz
    mkdir trnascan
    tar -zxf trnascan.tar.gz \
        -C trnascan \
        --strip-components 1
    cd trnascan || exit 1
    ./configure
    make && make install
    cd .. || exit 1
    rm -r trnascan trnascan.tar.gz

    # glimmerhmm
    (
    wget -O glimmerhmm.tar.gz \
        --no-check-certificate \
    https://ccb.jhu.edu/software/glimmerhmm/dl/GlimmerHMM-3.0.4.tar.gz
    mkdir glimmerhmm
    tar -zxf glimmerhmm.tar.gz \
        -C glimmerhmm \
        --strip-components 1
    cd glimmerhmm || exit 1

    # from here, follow the conda recipe from https://raw.githubusercontent.com/bioconda/bioconda-recipes/master/recipes/glimmerhmm/build.sh
    export PREFIX=/usr/local
    # fix typos in train makefile
    sed -i.bak "s|^escoreSTOP2:|scoreSTOP2:|g" train/makefile
    sed -i.bak "s|^rfapp:|erfapp:|g" train/makefile
    sed -i.bak "s| trainGlimmerHMM||g" train/makefile
    sed -i.bak "s|all:    build-icm|all:    misc.o build-icm.o build-icm-noframe.o build-icm|g" train/makefile

    # fix perl scripts
    sed -i.bak '1 s|^.*$|#!/usr/bin/env perl|g' train/trainGlimmerHMM
    sed -i.bak 's|FindBin;|FindBin qw($RealBin);|g' train/trainGlimmerHMM
    sed -i.bak 's|$FindBin::Bin;|"$RealBin/../share/glimmerhmm/train";|g' train/trainGlimmerHMM
    sed -i.bak '1 s|^.*$|#!/usr/bin/env perl|g' bin/glimmhmm.pl

    # make directories for storing training data and binaries
    mkdir -p $PREFIX/bin
    mkdir -p $PREFIX/share/glimmerhmm
    mkdir -p $PREFIX/share/glimmerhmm/train

    # make
    make -C sources
    make -C train clean && make -C train all

    # make executable
    chmod -R 755 .

    # copy the executables  
    cp bin/glimmhmm.pl $PREFIX/bin/
    cp sources/glimmerhmm $PREFIX/bin/
    cp train/trainGlimmerHMM $PREFIX/bin/
    cp train/build-icm $PREFIX/share/glimmerhmm/train/
    cp train/build-icm-noframe $PREFIX/share/glimmerhmm/train/
    cp train/build1 $PREFIX/share/glimmerhmm/train/
    cp train/build2 $PREFIX/share/glimmerhmm/train/
    cp train/erfapp $PREFIX/share/glimmerhmm/train/
    cp train/falsecomp $PREFIX/share/glimmerhmm/train/
    cp train/findsites $PREFIX/share/glimmerhmm/train/
    cp train/karlin $PREFIX/share/glimmerhmm/train/
    cp train/score $PREFIX/share/glimmerhmm/train/
    cp train/score2 $PREFIX/share/glimmerhmm/train/
    cp train/scoreATG $PREFIX/share/glimmerhmm/train/
    cp train/scoreATG2 $PREFIX/share/glimmerhmm/train/
    cp train/scoreSTOP $PREFIX/share/glimmerhmm/train/
    cp train/scoreSTOP2 $PREFIX/share/glimmerhmm/train/
    cp train/splicescore $PREFIX/share/glimmerhmm/train/

    # copy the perl modules
    cp train/*.pm $PREFIX/share/glimmerhmm/train/

    # copy the training data
    cp -R trained_dir $PREFIX/share/glimmerhmm/

    cd ../ || exit 1
    rm -r glimmerhmm.tar.gz glimmerhmm
    )

    # missing at 1.8.0
    # augustus (it's installed, not sure what the error is)
    # proteinortho not installed, don't know what it is
    # salmon (it's installed at /usr/bin/salmon)
    # signalp not installed, can't b/c license
    # trimmomatic (it's installed, java -jar /usr/share/java/trimmomatic.jar,
    #              /usr/bin/TrimmomaticPE, /usr/bin/TrimmomaticSE)
```

## Collection

 - Name: [TomHarrop/funannotate-singularity](https://github.com/TomHarrop/funannotate-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

