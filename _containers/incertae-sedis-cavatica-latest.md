---
id: 3906
name: "incertae-sedis/cavatica"
branch: "master"
tag: "latest"
commit: "f4fe278de8d2b5cc0b1a3cd0b5b4822a9336edf5"
version: "4110f0b27a42c198625afa0aac438e09"
build_date: "2018-08-09T02:18:32.499Z"
size_mb: 1182
size: 556273695
sif: "https://datasets.datalad.org/shub/incertae-sedis/cavatica/latest/2018-08-09-f4fe278d-4110f0b2/4110f0b27a42c198625afa0aac438e09.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/incertae-sedis/cavatica/latest/2018-08-09-f4fe278d-4110f0b2/
recipe: https://datasets.datalad.org/shub/incertae-sedis/cavatica/latest/2018-08-09-f4fe278d-4110f0b2/Singularity
collection: incertae-sedis/cavatica
---

# incertae-sedis/cavatica:latest

```bash
$ singularity pull shub://incertae-sedis/cavatica:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu
%post
    apt-get -y update
    apt-get install -y git
    git clone -b singularity_implementation https://github.com/TeamMango/cavatica.git
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

 - Name: [incertae-sedis/cavatica](https://github.com/incertae-sedis/cavatica)
 - License: None

