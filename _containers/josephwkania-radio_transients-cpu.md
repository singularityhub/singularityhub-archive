---
id: 15653
name: "josephwkania/radio_transients"
branch: "master"
tag: "cpu"
commit: "a6bd509b3d3c2140a3af44d1dded343fb3238e3e"
version: "43ed723b8e5dd632b561065de733f16ca13186d8732a693f6d6021cffc2fa791"
build_date: "2021-03-17T04:53:40.158Z"
size_mb: 1084.6484375
size: 1137336320
sif: "https://datasets.datalad.org/shub/josephwkania/radio_transients/cpu/2021-03-17-a6bd509b-43ed723b/43ed723b8e5dd632b561065de733f16ca13186d8732a693f6d6021cffc2fa791.sif"
url: https://datasets.datalad.org/shub/josephwkania/radio_transients/cpu/2021-03-17-a6bd509b-43ed723b/
recipe: https://datasets.datalad.org/shub/josephwkania/radio_transients/cpu/2021-03-17-a6bd509b-43ed723b/Singularity
collection: josephwkania/radio_transients
---

# josephwkania/radio_transients:cpu

```bash
$ singularity pull shub://josephwkania/radio_transients:cpu
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:20.04


%post
    echo "Installing packages needed for multiple programs"
    apt-get -y update
    apt-get -y install build-essential cmake git htop software-properties-common wget # need these to build pacakges
    
    apt-add-repository multiverse # add the multiverse repository (where pgplot5 lives)
    apt-get -y install pgplot5 
    export PGPLOT_DIR=/usr/lib/pgplot5

    # apt-get -y install python3 python-is-python3 python3-pip # use conda instead
    apt-get -y install libfftw3-dev libfftw3-bin libcfitsio-dev # We need these packages for multiple programs
    
    # use conda so everthing is compatiable with the cuda-10-2 container
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh -q
    bash ~/miniconda.sh -b -p /usr/local/miniconda
    rm ~/miniconda.sh
    eval "$(/usr/local/miniconda/bin/conda shell.bash hook)"
    conda init
    conda create -y --name RT python=3.7
    conda activate RT 
 
    # As described in https://github.com/hpcng/singularity/issues/5075#issuecomment-594391772
    echo "## Activate RT environment" >> /.singularity_bash
    echo "source /usr/local/miniconda/etc/profile.d/conda.sh" >> /.singularity_bash
    echo "conda activate RT" >> /.singularity_bash

    pip install numpy # make sure pip numpy get installed to avoid presto python error

    echo "Installing iqrm_apollo"
    cd ~
    apt-get -y install libboost1.67-all-dev # iqrm does not like 1.71 versions
    git clone https://gitlab.com/kmrajwade/iqrm_apollo.git
    cd iqrm_apollo
    mkdir build; cd build
    git checkout 4b8847ecd702eed582e1d28411e96a6d650a432f # This is the last commit I can get to make
    # see https://gitlab.com/kmrajwade/iqrm_apollo/-/issues/1
    cmake -DBOOST_ROOT=/ ../
    make -j
    cp iqrm_apollo/iqrm_apollo_cli /usr/local/bin/
    echo "Built iqrm_apollo at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)" 
    cd ~ && rm -rf iqrm_apollo    

    echo "Installing juyterlab"
    # pip3 install jupyterlab
    conda install -y -c conda-forge jupyterlab

    echo "Installing Tempo"
    cd /usr/local #put file here so we can access them later
    apt-get -y install csh autoconf gfortran
    git clone git://git.code.sf.net/p/tempo/tempo
    cd tempo
    ./prepare
    ./configure
    make
    make install
    export TEMPO=$PWD # Presto need to know this
    echo "Built Tempo at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"

    echo "Installing PRESTO"
    # mkdir /usr/local/
    cd /usr/local/
    apt-get -y install libglib2.0-dev libpng-dev libx11-dev mpich 
    git clone https://github.com/scottransom/presto.git
    cd presto
    export PRESTO=$PWD
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PRESTO/lib
    cd $PRESTO/src # links libsla, thanks https://github.com/scottransom/presto/issues/1#issuecomment-60413231
    make prep
    make
    make mpi
    make clean
    cd $PRESTO
    # pip install  numpy # installed at top
    sed -i '' $PRESTO/python/presto/waterfaller.py # removes symbolic link (which upsets pip) https://stackoverflow.com/a/12673543
    pip install .
    cp $PRESTO/bin/* /usr/local/bin
    echo "Built PRESTO at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"    

    echo "Installing psrcat"
    cd ~
    apt-get -y install tcsh
    wget https://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz
    tar xf psrcat_pkg.tar.gz 
    cd psrcat_tar
    tcsh makeit
    mv psrcat /usr/local/bin
    mv *.db /usr/local
    echo "Built psrcat"
    cd ~ && rm -rf psrcat_tar 

    echo "Installing pysigproc"
    cd ~
    git clone https://github.com/devanshkv/pysigproc.git
    cd pysigproc
    pip install . 
    echo "Built RFICLean at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf pysigproc

    echo "Installing rficlean"
    cd ~
    # git clone https://github.com/josephwkania/RFIClean.git
    git clone https://github.com/ymaan4/RFIClean.git 
    cd RFIClean
    mkdir -p /home/maan/pulsar_softwares/bin
    make
    make install
    mv /home/maan/pulsar_softwares/bin/* /usr/local/bin
    rm -r /home/maan
    echo "Built RFICLean at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf RFIClean 

    echo "Installing riptide"
    pip install riptide-ffa
 
    echo "Installing sigproc"
    cd ~
    git clone https://github.com/SixByNine/sigproc.git
    cd sigproc
    ./bootstrap
    ./configure --prefix=/usr/local/
    make
    make install
    echo "Built sigproc at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf sigproc

    echo "Installing YAPP"
    cd ~
    apt-get -y install libhdf5-dev
    mkdir -p /usr/local/hdf5
    ln -s /usr/include/hdf5/serial /usr/local/hdf5/include
    mkdir -p /usr/local/hdf5
    ln -s /usr/lib/x86_64-linux-gnu/hdf5/serial/lib /usr/local/hdf5/lib
    git clone https://github.com/jayanthc/yapp.git
    cd yapp 
    make HDF5=yes
    make install
    echo "Built YAPP at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf yapp    

    echo "Installing your"
    cd ~
    git clone https://github.com/thepetabyteproject/your.git
    cd your
    pip install .
    echo "Built your at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf your        

    # This wants to remove libboost, which we need
    #apt-get -y purge cmake build-essential git wget # remove build time dependencies
    #apt-get -y autoremove 
    apt-get -y clean # /var/cache/apt/archives is not emptied on its own, 
    conda clean --all

    echo "Done building!"


%environment
    # For conda
    action="${0##*/}"
    if [ "$action" = "shell" ]; then
        if [ "${SINGULARITY_SHELL:-}" = "/bin/bash" ]; then
            set -- --noprofile --init-file /.singularity_bash
        elif test -z "${SINGULARITY_SHELL:-}"; then
            export SINGULARITY_SHELL=/bin/bash
            set -- --noprofile --init-file /.singularity_bash
        fi
    fi
    
    source /usr/local/miniconda/bin/activate RT # sets up conda so we can access outside the continer

    export PGPLOT_DIR=/usr/lib/pgplot5
    export TEMPO=/usr/local/tempo
    export PRESTO=/usr/local/presto
    export LD_LIBRARY_PATH=$PRESTO/lib:$LD_LIBRARY_PATH
    export PSRCAT_FILE=/usr/local/psrcat.db


%runscript
    exec /usr/local/miniconda/RT/bin/"$@"
    exec /bin/bash --noprofile --init-file /.singularity_bash "$@"


%help
    This container has CPU software to search for radio transients.
        
    Contains the following programs:
    htop          https://htop.dev/
    iqrm_apollo   https://gitlab.com/kmrajwade/iqrm_apollo
    jupyterlab    https://jupyter.org/
    PRESTO        https://www.cv.nrao.edu/~sransom/presto/
    psrcat        https://www.atnf.csiro.au/people/pulsar/psrcat/download.html
    pysigproc     https://github.com/devanshkv/pysigproc
    riptide       https://github.com/v-morello/riptide
    sigproc       https://github.com/SixByNine/sigproc
    Tempo         http://tempo.sourceforge.net/
    RFIClean      https://github.com/ymaan4/RFIClean
    YAPP          https://github.com/jayanthc/yapp
    your          https://github.com/thepetabyteproject/your


%labels
    Author Joseph W Kania
    Version v0.0.3
```

## Collection

 - Name: [josephwkania/radio_transients](https://github.com/josephwkania/radio_transients)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

