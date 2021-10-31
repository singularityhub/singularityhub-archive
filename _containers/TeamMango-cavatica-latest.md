---
id: 3704
name: "TeamMango/cavatica"
branch: "master"
tag: "latest"
commit: "d74b9b3b1db5a5b3c802518d9541d982f486e2eb"
version: "e3b10270f19c624733d97c919496ffeb"
build_date: "2018-07-26T20:24:37.662Z"
size_mb: 1182
size: 556167199
sif: "https://datasets.datalad.org/shub/TeamMango/cavatica/latest/2018-07-26-d74b9b3b-e3b10270/e3b10270f19c624733d97c919496ffeb.simg"
url: https://datasets.datalad.org/shub/TeamMango/cavatica/latest/2018-07-26-d74b9b3b-e3b10270/
recipe: https://datasets.datalad.org/shub/TeamMango/cavatica/latest/2018-07-26-d74b9b3b-e3b10270/Singularity
collection: TeamMango/cavatica
---

# TeamMango/cavatica:latest

```bash
$ singularity pull shub://TeamMango/cavatica:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%labels
    author Jennifer Chang
    title Cavatica: A pipeline for identifying author adoption trends among software or methods
    doi 10.1109/BIBM.2017.8217990
    last-update 2018-07-26
%post
    apt-get -y update
    apt-get install -y git
    git clone https://github.com/TeamMango/cavatica.git
    chmod -R go+rw /cavatica/ 
    DEBIAN_FRONTEND=noninteractive apt-get install -y r-base 
    echo "install.packages(\"ggplot2\", repos=\"https://cran.rstudio.com\")" | R --no-save
    echo "install.packages(\"readr\", repos=\"https://cran.rstudio.com\")" | R --no-save
%runscript    
    cd /cavatica/data/output
    ln -s ../test/*.tsv .
    ../../code/script.sh
    find /cavatica/data/output -type l | xargs rm
%environment
    export PATH=/:$PATH
```

## Collection

 - Name: [TeamMango/cavatica](https://github.com/TeamMango/cavatica)
 - License: None

