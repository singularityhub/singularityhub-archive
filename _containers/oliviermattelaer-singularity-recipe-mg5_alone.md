---
id: 5631
name: "oliviermattelaer/singularity-recipe"
branch: "master"
tag: "mg5_alone"
commit: "4d88419507a86c74364e326c7dc466e3470721e8"
version: "b5881eb6db6b0b80650c3e5fbe458d5c"
build_date: "2020-10-08T15:32:49.439Z"
size_mb: 4727
size: 2225135647
sif: "https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/mg5_alone/2020-10-08-4d884195-b5881eb6/b5881eb6db6b0b80650c3e5fbe458d5c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/oliviermattelaer/singularity-recipe/mg5_alone/2020-10-08-4d884195-b5881eb6/
recipe: https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/mg5_alone/2020-10-08-4d884195-b5881eb6/Singularity
collection: oliviermattelaer/singularity-recipe
---

# oliviermattelaer/singularity-recipe:mg5_alone

```bash
$ singularity pull shub://oliviermattelaer/singularity-recipe:mg5_alone
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%runscript
    /usr/mg5amcnlo/bin/mg5_aMC


%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install emacs bzr python2.7 gcc gfortran g++ make python-pip wget gnuplot bc cmake
    pip install numpy scipy
    # MA5 specific
    apt-get -y install texlive-latex-base rlwrap latex-xcolor python-tk
    pip install matplotlib
    
    cd /usr
    wget https://bazaar.launchpad.net/~mg5core1/mg5amcnlo/2.6.5/tarball/283
    echo "install lhapdf6;" > cmd
    echo "install MadAnalysis5;" >> cmd
    echo "install maddm;" >> cmd
    echo "generate p p > t t~; output /tmp/proc;" >> cmd
    tar -xzpvf 283
    mv ~mg5core1/mg5amcnlo/2.6.5  mg5amcnlo
    rm -rf 283
    ./mg5amcnlo/bin/mg5 cmd

    # Set up graphic renderer for MA5:
    cd /usr/mg5amcnlo/HEPTools/madanalysis5/madanalysis5/madanalysis/layout/
    sed -i "s/#        outputPy.write(\"    matplotlib.use/        outputPy.write(\"    matplotlib.use/" plotflow.py
    # avoid the change in the library:
    cd /usr/mg5amcnlo/HEPTools/madanalysis5/madanalysis5/madanalysis/core/
    sed -i "s/UpdateNeed=True/UpdateNeed=False/" main.py
    cd /usr/mg5amcnlo/HEPTools/madanalysis5/madanalysis5/madanalysis/misc/
    sed  -i "s/raise/pass#/" freeze_environment.py

    # looptools (since cmake is present now)
    cd /usr
    echo "install looptools;" > cmd2
    echo "generate g g > t t~ [QCD]; output" >> cmd2
    ./mg5amcnlo/bin/mg5 cmd2

    # directory for UFOMODEL loading (to be linked to a directory via singularity)
    mkdir /UFO

%environment
   export LC_ALL=C
   export PYTHONPATH=$PYTHONPATH:/usr/mg5amcnlo/HEPTools/lhapdf6/lib/python2.7/site-packages
   export LD_LIBRARY_PATH=/usr/mg5amcnlo/HEPTools/lhapdf6/lib:/usr/mg5amcnlo/HEPTools/lib/:$LD_LIBRARY_PATH
   export LHAPATH=/tmp
   export PATH=$ROOTSYS/bin:$PATH
   #FOR UFOMODEL
   export PYTHONPATH=$PYTHONPATH:/UFO
```

## Collection

 - Name: [oliviermattelaer/singularity-recipe](https://github.com/oliviermattelaer/singularity-recipe)
 - License: None

