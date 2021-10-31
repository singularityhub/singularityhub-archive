---
id: 15197
name: "pchengi/cmorfixer_env"
branch: "master"
tag: "latest"
commit: "65a35041f4f8f8f31da50fb3f667b41b3fee25a9"
version: "ae4eab894817a871bae324bfd2898512"
build_date: "2021-01-21T18:18:31.626Z"
size_mb: 1991.0
size: 845430815
sif: "https://datasets.datalad.org/shub/pchengi/cmorfixer_env/latest/2021-01-21-65a35041-ae4eab89/ae4eab894817a871bae324bfd2898512.sif"
url: https://datasets.datalad.org/shub/pchengi/cmorfixer_env/latest/2021-01-21-65a35041-ae4eab89/
recipe: https://datasets.datalad.org/shub/pchengi/cmorfixer_env/latest/2021-01-21-65a35041-ae4eab89/Singularity
collection: pchengi/cmorfixer_env
---

# pchengi/cmorfixer_env:latest

```bash
$ singularity pull shub://pchengi/cmorfixer_env:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian

%files
    scripts/ /opt/
    cmor_fixer/ /opt/

%post
    apt-get update && apt-get install -y git wget make libssl-dev libpython3-dev build-essential vim screen bash
    cd /opt/cmor_fixer
    export SHELL=/bin/bash
    git clone https://github.com/pchengi/cmor-fixer.git
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -u -p /opt/cmor_fixer/miniconda3
    echo 'miniconda3path=/opt/cmor_fixer/miniconda3/' >>/etc/bashrc
    echo "alias activateminiconda3='source /opt/cmor_fixer/miniconda3/etc/profile.d/conda.sh'" >>/etc/bashrc
    /bin/bash -c 'source /etc/bashrc'
    /bin/bash -c 'source /opt/cmor_fixer/miniconda3/etc/profile.d/conda.sh'
    /bin/bash -c '/opt/cmor_fixer/miniconda3/bin/conda update -y -n base -c defaults conda'
    cd cmor-fixer && git checkout check-output-filename
    /bin/bash -c '/opt/cmor_fixer/miniconda3/bin/conda env create -f environment.yml'
```

## Collection

 - Name: [pchengi/cmorfixer_env](https://github.com/pchengi/cmorfixer_env)
 - License: None

