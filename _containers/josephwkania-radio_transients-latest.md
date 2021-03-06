---
id: 15652
name: "josephwkania/radio_transients"
branch: "master"
tag: "latest"
commit: "196ce4bfc2063502a9eb907e44ace788f3d88c89"
version: "bbe343ed6ae704f5ccd6af4e018b46f6a45c50933b108129371e5f381def1f7e"
build_date: "2021-04-16T16:44:05.065Z"
size_mb: 4040.55078125
size: 4236824576
sif: "https://datasets.datalad.org/shub/josephwkania/radio_transients/latest/2021-04-16-196ce4bf-bbe343ed/bbe343ed6ae704f5ccd6af4e018b46f6a45c50933b108129371e5f381def1f7e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/josephwkania/radio_transients/latest/2021-04-16-196ce4bf-bbe343ed/
recipe: https://datasets.datalad.org/shub/josephwkania/radio_transients/latest/2021-04-16-196ce4bf-bbe343ed/Singularity
collection: josephwkania/radio_transients
---

# josephwkania/radio_transients:latest

```bash
$ singularity pull shub://josephwkania/radio_transients:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From:  nvidia/cuda:10.2-devel # Needed for fetch
# I think this is ~ubuntu 18 base


%post
    apt-get update # update and install packages we need for the build
    apt-get -y install autoconf build-essential cmake csh git htop libboost-all-dev libtool libtool-bin python2.7 software-properties-common wget
    # need these to build pacakges

    apt-add-repository multiverse # add the multiverse repository (where pgplot5 lives)
    apt-get -y install pgplot5
    export PGPLOT_DIR=/usr/lib/pgplot5

    apt-get -y install python3 python3-pip # PRESTO needs its own python env separate from FETCH, else PRESTO fails
    apt-get -y install libfftw3-dev libfftw3-bin libcfitsio-dev # We need these packages for multiple programs
    
    # I can't get your to build in ubuntu's python3.7, llvmlite fails and there is no clear way around this
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh -q
    bash ~/miniconda.sh -b -p /usr/local/miniconda
    rm ~/miniconda.sh
    eval "$(/usr/local/miniconda/bin/conda shell.bash hook)"
    conda init
    conda create -y --name RT python=3.7
    conda create -y --name PE python=3.7
    conda activate RT
        
    # As described in https://github.com/hpcng/singularity/issues/5075#issuecomment-594391772
    echo "## Activate RT environment" >> /.singularity_bash
    echo "source /usr/local/miniconda/etc/profile.d/conda.sh" >> /.singularity_bash
    echo "conda activate RT" >> /.singularity_bash

    # moved FETCH install to last, try to minimize the impact of conda installs on presto 

    # Dirs for Heimdall build
    mkdir ~/source # build soft
    mkdir ~/software # put binaries here

    echo "Building Dedisp"
    mkdir -p /root/software/dedisp/include # dedisp need these
    mkdir -p /root/software/dedisp/lib/

    cd ~/source
    git clone https://github.com/ajameson/dedisp.git
    cd dedisp
    make INSTALL_DIR=$HOME/software/dedisp install
    cp ~/software/dedisp/lib/* /usr/local/lib
    export LD_LIBRARY_PATH=LD_LIBRARY_PATH:~/software/dedisp
    echo "built dedisp at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"

    echo "Building Psrdada"
    cd ~/source
    export CFLAGS="-fopenmp -fPIC"
    git clone https://git.code.sf.net/p/psrdada/code psrdada
    cd psrdada
    ./bootstrap
    ./configure --prefix=$HOME/software/psrdada
    make
    make install
    cp -r ~/software/psrdada/bin/* /usr/local/bin
    cp -r ~/software/psrdada/lib/* /usr/local/lib
    cp -r ~/software/psrdada/include/* /usr/include
    echo "built psrdada at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"

    export PATH=$PATH:/usr/local/cuda
    echo "Building Heimdall"
    cd ~/source
    #ln -s /usr/bin/python2.7 /usr/bin/python # needs py27 to build
    git clone git://git.code.sf.net/p/heimdall-astro/code heimdall
    cd heimdall
    ./bootstrap
    ./configure --prefix=$HOME/software/heimdall/linux_64 --with-psrdada-dir=$HOME/software/psrdada --with-dedisp-dir=$HOME/software/dedisp --with-cuda-dir=/usr/local/cuda
    sed -i -e 's+-I/root/software/psrdada/include -fopenmp+-I/root/software/psrdada/include+' Pipeline/Makefile
    # sed -n 92p Pipeline/Makefile check if line is changed
    make install
    mv ~/software/heimdall/linux_64/bin/* /usr/local/bin
    echo "built Heimdall at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"

    # rm /usr/bin/python # don't need python linked after heimdall is built
    rm -rf software source # clean up after heimdall build

    echo "Installing iqrm_apollo"
    cd ~
    git clone https://gitlab.com/kmrajwade/iqrm_apollo.git
    cd iqrm_apollo
    mkdir build; cd build
    git checkout 4b8847ecd702eed582e1d28411e96a6d650a432f # This is the last commit I can get to make
    cmake -DBOOST_ROOT=/ ../
    make -j
    cp iqrm_apollo/iqrm_apollo_cli /usr/local/bin/
    echo "Built iqrm_apollo at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf iqrm_apollo

    echo "Installing juyterlab"
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
    conda activate PE # But PRESTO in its own env, so FETCH doen't cause problems
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
    pip install numpy
    #/usr/bin/pip3 install numpy # not in requiments file
    #conda install -y numpy
    sed -i '' $PRESTO/python/presto/waterfaller.py # removes symbolic link (which upsets pip) https://stackoverflow.com/a/12673543
    pip install .
    mv $PRESTO/bin/* /usr/local/bin
    conda activate RT
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

    echo "Installing psrdada-python"
    cd ~
    git clone https://github.com/TRASAL/psrdada-python.git
    cd psrdada-python
    pip install -r requirements.txt
    # add lib and include paths to setup.py
    sed -i "51 a LIBRARY_DIRS.append('/usr/local/lib')" setup.py
    sed -i "51 a INCLUDE_DIRS.append('/usr/include')" setup.py
    make
    make install
    echo "built psrdada-python at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf psrdada-python

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

    echo "Building FETCH"
    conda install -y -c anaconda cudatoolkit==10.0.130 tensorflow-gpu==1.13.1
    conda install -y -c anaconda keras scikit-learn pandas scipy numpy matplotlib scikit-image tqdm numba pyyaml==3.13
    git clone https://github.com/devanshkv/fetch.git
    cd fetch
    pip install .
    echo "built dedisp at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf fetch

    #apt-get -y purge autoconf build-essential cmake git python2.7 wget # remove build time dependencies
    #apt-get -y autoremove
    apt-get -y clean # /var/cache/apt/archives is not emptied on its own
    conda clean --all

    echo "Done building"


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
   
    export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH # dedisp libs
   
    export QT_QPA_PLATFORM=offscreen # allows your_viewer to run when --nv is given, see https://github.com/therecipe/qt/issues/775#issuecomment-475900676

%runscript
    exec your_heimdall.py
    # exec /usr/local/miniconda/RT/bin/"$@"
    # exec /bin/bash --noprofile --init-file /.singularity_bash "$@"


%help
    This container has software to search for radio transients.

    Contains the following programs:
    CUDA 10.2
    fetch          https://github.com/devanshkv/fetch
    heimdall       https://sourceforge.net/p/heimdall-astro/wiki/Use/
    - dedisp       https://github.com/ajameson/dedisp
    htop           https://htop.dev/
    iqrm_apollo    https://gitlab.com/kmrajwade/iqrm_apollo
    jupyterlab     https://jupyter.org/
    PRESTO         https://www.cv.nrao.edu/~sransom/presto/
    psrdada        http://psrdada.sourceforge.net/
    psrdada-python https://github.com/TRASAL/psrdada-python
    psrcat         https://www.atnf.csiro.au/people/pulsar/psrcat/download.html
    pysigproc      https://github.com/devanshkv/pysigproc
    riptide        https://github.com/v-morello/riptide
    sigproc        https://github.com/SixByNine/sigproc
    Tempo          http://tempo.sourceforge.net/
    RFIClean       https://github.com/ymaan4/RFIClean
    YAPP           https://github.com/jayanthc/yapp
    your           https://github.com/thepetabyteproject/your
    

%labels
    Author Joseph W Kania
    Version v0.0.3
```

## Collection

 - Name: [josephwkania/radio_transients](https://github.com/josephwkania/radio_transients)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

