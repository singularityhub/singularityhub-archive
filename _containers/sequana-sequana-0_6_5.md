---
id: 4672
name: "sequana/sequana"
branch: "master"
tag: "0_6_5"
commit: "b77d7b93f25fa687b7a4934ded11f698a175fefc"
version: "311924a02b0069ead6f08170963b7631"
build_date: "2020-07-24T12:10:09.860Z"
size_mb: 4948
size: 1635520543
sif: "https://datasets.datalad.org/shub/sequana/sequana/0_6_5/2020-07-24-b77d7b93-311924a0/311924a02b0069ead6f08170963b7631.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sequana/sequana/0_6_5/2020-07-24-b77d7b93-311924a0/
recipe: https://datasets.datalad.org/shub/sequana/sequana/0_6_5/2020-07-24-b77d7b93-311924a0/Singularity
collection: sequana/sequana
---

# sequana/sequana:0_6_5

```bash
$ singularity pull shub://sequana/sequana:0_6_5
```

## Singularity Recipe

```singularity
#BootStrap: debootstrap
#DistType "debian"
#MirrorURL: http://us.archive.ubuntu.com/ubuntu/
#OSVersion: xenial
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR Thomas Cokelaer

%post

    apt-get update
    apt-get install -y wget
    apt-get install -y bzip2
    apt-get install -y vim
    apt-get install -y libgl1-mesa-glx  # will be required by pyqt
    apt-get install -y fontconfig # for sequanix/qt fonts otherwise no text in menus

    # for fastqc
    apt-get install -y libxrender1
    apt-get install -y libxtst6
    apt-get install -y libxi6

    # for sequanix (Qt plugin) otherwise libxcb missing
    apt-get install -y libsm-dev
    apt-get install -y libxcomposite-dev

    # This is a large data set again. When using the container a sroot, sequanix
    # looks good but in normal mode, the menu is blank...and this seems to solve
    # the issue
    apt-get install -y libgnomeui-0

    # on some system, there is waning message about dvipng missing
    #apt-get install -y dvipng

    # avoid warning
    #  Gtk-Message: Failed to load module "pk-gtk-module"
    #  Gtk-Message: Failed to load module "canberra-gtk-module"
    apt-get install -y libcanberra-gtk-module
    apt-get install -y packagekit-gtk3-module

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
        #wget https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh\
        # for now, we use 4.2.12 to have python3.5 by default so no need to
        # create a new env saving space in the process. The reason for using 3.5
        # is inherent to the packages used at the moment.
        wget https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh\
           -O ~/anaconda.sh && \
        bash ~/anaconda.sh -b -p /usr/local/anaconda && \
        rm ~/anaconda.sh
    fi

    # set anaconda path
    export PATH=$PATH:/usr/local/anaconda/bin
    conda update conda

    conda config --add channels r
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

    # The main packages for sequana:
    conda install --file https://raw.githubusercontent.com/sequana/sequana/master/requirements.txt

    # the packages for various pipelines
    conda install --file https://raw.githubusercontent.com/sequana/sequana/master/requirements_pipelines.txt

    # Let us save some space
    conda clean --packages -y

    # For the pipelines_extra, busco takes for ever, so we skip it for now
    conda install -y canu
    # this one hangs for ever busco==3.0.2
    # conda install -y prokka # takes lots of place

    # Let us save some space
    conda clean --packages -y

    # Sequana source code
    pip install sequana==0.6.5.post3

    conda clean --all -y # next requires lots of space
    rm -rf /usr/local/anaconda/pkgs

    # pysam/bzip/hstlib is tricky. We pin versions as follows
    conda install --override-channels -c conda-forge bzip2
    conda install --override-channels -c bioconda -c conda-forge htslib==1.5.0
    conda install pysam==0.12.0.1

    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /scripts ]; then mkdir /scripts; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi
    if [ ! -d /mounting ]; then mkdir /mounting; fi
    # temporary fix for IP cluster
    if [ ! -d /pasteur ]; then mkdir /pasteur; fi
    echo "backend:tkagg" > matplotlibrc

    export PATH=$PATH:/usr/local/anaconda/bin
    export LANG=C   # prevents perl for raising warnings
    export PERL5LIB=/usr/local/anaconda/lib/perl5/5.22.0
    python -c "import sequana" # creates config file and check installation


%environment
    export PATH=$PATH:/usr/local/anaconda/bin
    export LANG=C   # prevents perl for raising warnings
    export PERL5LIB=/usr/local/anaconda/lib/perl5/5.22.0
    # Issue with multiqc/click should be solved with those 2 exports
    # This one raises a warning: Error: Fontconfig warning: ignoring C.UTF-8:
    # not a valid language tag.
    #export LANG=C.UTF-8
    #export LC_ALL=C.UTF-8
    # according to https://github.com/uncss/uncss/issues/166, should use
    #export LC_ALL=C  but does not work ! Same error as above
    export LC_ALL=C.UTF-8


    #echo "backend:agg" > matplotlibrc
```

## Collection

 - Name: [sequana/sequana](https://github.com/sequana/sequana)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

