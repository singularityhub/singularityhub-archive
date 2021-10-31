---
id: 6666
name: "icaoberg/singularity-latex"
branch: "master"
tag: "latest"
commit: "1a6192a72c87a84ab1020cb91c0d68ec11428d97"
version: "ceece513087fefd42a16ebee7f083446"
build_date: "2021-03-30T15:52:34.045Z"
size_mb: 4574
size: 2616680479
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-latex/latest/2021-03-30-1a6192a7-ceece513/ceece513087fefd42a16ebee7f083446.simg"
url: https://datasets.datalad.org/shub/icaoberg/singularity-latex/latest/2021-03-30-1a6192a7-ceece513/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-latex/latest/2021-03-30-1a6192a7-ceece513/Singularity
collection: icaoberg/singularity-latex
---

# icaoberg/singularity-latex:latest

```bash
$ singularity pull shub://icaoberg/singularity-latex:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

IncludeCmd: yes

%runscript
    exec /usr/bin/python "$@"

%post
    #runs apt-get install for the package, -y being auto-yes and -q being quiet
    /usr/bin/apt-get update && /usr/bin/apt-get -y upgrade
    /usr/bin/apt-get update --fix-missing
    /usr/bin/apt-get install -y --no-install-recommends apt-utils
    /usr/bin/apt-get install -yq texlive-full texmaker --no-install-recommends
    /usr/bin/apt-get install -yq lyx

    #texmacs
    #/usr/bin/apt-get install -yq wget
    #/bin/gunzip -c TeXmacs-1.99.9-C.tar.gz | tar xvf -

    if [ ! -d /images ]; then mkdir /images; fi
    if [ ! -d /projects ]; then mkdir /projects; fi
    if [ ! -d /containers ]; then mkdir /containers; fi
    if [ ! -d /share ]; then mkdir /share; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi

################### PDFTEX ###################
%appenv pdftex
    BEST_APP=pdftex
    export BEST_APP

%apphelp pdftex
    For more information about pdftex please visit
 
    * https://www.tug.org/applications/pdftex/

%apprun pdftex
    pdftex "$@"

################ GHOSTSCRIPT #################
%appenv gs
    BEST_APP=gs
    export BEST_APP

%apphelp gs
    For more information about pdftex please visit

    * https://www.ghostscript.com/ 

%apprun gs
    gs "$@"

################### LATEX ####################
%appenv latex
    BEST_APP=latex
    export BEST_APP

%apphelp latex
    For more information about pdftex please visit
 
    * https://www.latex-project.org/

%apprun latex
    latex "$@"

################## PDFLATEX ##################
%appenv pdflatex
    BEST_APP=pdflatex
    export BEST_APP

%apphelp pdflatex
    For more information about pdftex please visit
 
    * https://www.tug.org/applications/pdftex/

%apprun pdflatex
    pdflatex "$@"

#################### ETEX #####################
%appenv etex
    BEST_APP=etex
    export BEST_APP

%apphelp etex
    For more information about pdftex please visit
 
    * https://www.tug.org/applications/pdftex/

%apprun etex
    etex "$@"

################### TEXMAKER ####################
%appenv texmaker
    BEST_APP=/usr/bin/texmaker
    export BEST_APP

%apphelp texmaker
    For more information about pdftex please visit
 
    * http://www.xm1math.net/texmaker/

%apprun texmaker
    texmaker "$@"

################### LYX ####################
%appenv lyx
    BEST_APP=lyx
    export BEST_APP
    
%apphelp lyx
    For more information about lyx please visit
    
    * https://www.lyx.org
    
%apprun lyx
    lyx "$@"
    
#texmacs goes here
#%appenv texmacs
#BEST_APP=texmacs
#export BEST_APP

#%apphelp texmacs
#help message here

#%apprun texmacs
#texmacs "$@"
```

## Collection

 - Name: [icaoberg/singularity-latex](https://github.com/icaoberg/singularity-latex)
 - License: None

