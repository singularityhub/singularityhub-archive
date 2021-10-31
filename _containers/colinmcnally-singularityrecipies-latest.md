---
id: 2739
name: "colinmcnally/singularityrecipies"
branch: "master"
tag: "latest"
commit: "9b19a51be799b2d775d4b835e31907d9c44c6d1e"
version: "5755ec0fc82be1a5174733d3693ddb0f"
build_date: "2019-11-08T15:27:15.456Z"
size_mb: None
size: 695300127
sif: "https://datasets.datalad.org/shub/colinmcnally/singularityrecipies/latest/2019-11-08-9b19a51b-5755ec0f/5755ec0fc82be1a5174733d3693ddb0f.simg"
url: https://datasets.datalad.org/shub/colinmcnally/singularityrecipies/latest/2019-11-08-9b19a51b-5755ec0f/
recipe: https://datasets.datalad.org/shub/colinmcnally/singularityrecipies/latest/2019-11-08-9b19a51b-5755ec0f/Singularity
collection: colinmcnally/singularityrecipies
---

# colinmcnally/singularityrecipies:latest

```bash
$ singularity pull shub://colinmcnally/singularityrecipies:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:disco

%post
    apt-get update -qq
    apt-get install wget software-properties-common apt-transport-https -y 
    apt-get install libosmesa6 -y
    apt-get install libglu1-mesa -y
    apt-get install dvipng -y
    apt-get install less -y
    apt-get install ipython3 -y
    apt-get install ipython3-qtconsole -y
    apt-get install python3-matplotlib -y
    apt-get install python3-h5py -y
    apt-get install python3-numpy -y
    apt-get install python3-mpi4py -y
    apt-get install python3-scipy -y
    apt-get install python3-pandas -y
    apt-get install python3-seaborn -y
    apt-get install python3-pip -y
    apt-get install texlive-latex-base -y
    apt-get install texlive-latex-extra -y
    apt-get install htop -y
    apt-get install git -y
    apt-get install mercurial -y
    apt-get install firefox -y
    apt-get install x2goserver -y
    apt-get install imagemagick -y
    apt-get install feh -y

# vmtouch requires root.
#    add-apt-repository ppa:likemartinma/devel
#    apt-get update
#    apt-get install vmtouch -y
    apt-get install vim -y

# these might not work in latest version
#    pip3 install plotly
#    pip3 install latexcodec
    pip3 install rebound
    
    # build the font cache
    python3 -c "import matplotlib.pyplot"
    
    hg clone https://colinmcnally@bitbucket.org/colinmcnally/pyevtk
    cd pyevtk
    python3 setup.py install

%runscript

    exec echo "runscript is empty "
```

## Collection

 - Name: [colinmcnally/singularityrecipies](https://github.com/colinmcnally/singularityrecipies)
 - License: None

