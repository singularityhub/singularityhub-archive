---
id: 15654
name: "josephwkania/radio_transients"
branch: "master"
tag: "gpu"
commit: "b78cdfadff2ddf3beae66d4abaf6ff477e4f2c57"
version: "af36c21a70bdfae286ba8f0f4100ad2de2a4718a756f0701f493ac95971b447f"
build_date: "2021-03-13T07:19:55.728Z"
size_mb: 3341.109375
size: 3503407104
sif: "https://datasets.datalad.org/shub/josephwkania/radio_transients/gpu/2021-03-13-b78cdfad-af36c21a/af36c21a70bdfae286ba8f0f4100ad2de2a4718a756f0701f493ac95971b447f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/josephwkania/radio_transients/gpu/2021-03-13-b78cdfad-af36c21a/
recipe: https://datasets.datalad.org/shub/josephwkania/radio_transients/gpu/2021-03-13-b78cdfad-af36c21a/Singularity
collection: josephwkania/radio_transients
---

# josephwkania/radio_transients:gpu

```bash
$ singularity pull shub://josephwkania/radio_transients:gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From:  nvidia/cuda:10.2-devel # Needed for fetch


%post
    apt-get update # update and install packages we need for the build
    apt-get -y install autoconf build-essential csh git htop libboost-dev libtool libtool-bin python2.7 software-properties-common wget
 
    # I can't get your to build in ubuntu's python3.7, llvmlite fails and there is no clear way around this
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
    
    echo "Building FETCH"
    conda install -y -c anaconda cudatoolkit==10.0.130 tensorflow-gpu==1.13.1
    conda install -y -c anaconda keras scikit-learn pandas scipy numpy matplotlib scikit-image tqdm numba pyyaml=3.13
    git clone https://github.com/devanshkv/fetch.git
    cd fetch
    pip install . 
    echo "built dedisp at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf fetch
    
    echo "Installing jupyterlab"
    # Not needed for any in particular, but might be useful
    conda install -y -c conda-forge jupyterlab

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
    export CFLAGS="-fopenmp -fPIC" # needs to be complied with fPIC for psrdada-python to work
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
    ln -s /usr/bin/python2.7 /usr/bin/python # needs py27 to build
    git clone git://git.code.sf.net/p/heimdall-astro/code heimdall
    cd heimdall
    ./bootstrap
    ./configure --prefix=$HOME/software/heimdall/linux_64 --with-psrdada-dir=$HOME/software/psrdada --with-dedisp-dir=$HOME/software/dedisp --with-cuda-dir=/usr/local/cuda
    sed -i -e 's+-I/root/software/psrdada/include -fopenmp+-I/root/software/psrdada/include+' Pipeline/Makefile
    # sed -n 92p Pipeline/Makefile check if line is changed
    make install
    mv ~/software/heimdall/linux_64/bin/* /usr/local/bin
    echo "built Heimdall at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
 
    rm /usr/bin/python # don't need python linked after heimdall is built
    rm -rf software source # clean up after heimdall build
    
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

    echo "Installing your"
    cd ~
    git clone https://github.com/thepetabyteproject/your.git
    cd your
    pip install .
    echo "built your at commit $(git rev-parse HEAD) which was on $(git log -1 --format=%cd)"
    cd ~ && rm -rf your

    apt-get -y purge autoconf build-essential git python2.7 wget # remove build time dependencies
    apt-get -y autoremove 
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

    export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH # dedisp libs 
  
    export QT_QPA_PLATFORM=offscreen # allows your_viewer to run when --nv is given, see https://github.com/therecipe/qt/issues/775#issuecomment-475900676


%runscript
    exec /usr/local/miniconda/RT/bin/"$@"
    exec /bin/bash --noprofile --init-file /.singularity_bash "$@"


%help
This container is for running your_heimdall on dada buffers for search for single pulses.
These pulses can be classified with FETCH. 

    Contains:
    CUDA 10.0         
    fetch          https://github.com/devanshkv/fetch
    jupyterlab     https://jupyter.org
    heimdall       https://sourceforge.net/p/heimdall-astro/wiki/Use/
    - dedisp       https://github.com/ajameson/dedisp
    htop           https://htop.dev/
    psrdada        http://psrdada.sourceforge.net/
    psrdada-python https://github.com/TRASAL/psrdada-python
    your           https://github.com/thepetabyteproject/your


%labels
    Author Joseph W Kania 
    Version v0.0.3
```

## Collection

 - Name: [josephwkania/radio_transients](https://github.com/josephwkania/radio_transients)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

