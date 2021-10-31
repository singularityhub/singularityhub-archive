---
id: 7575
name: "tobiasschlatter/BA-Eye-Tracking"
branch: "master"
tag: "latest"
commit: "985eed76ee76fdcdefe1cf1dc8f4741e906f2839"
version: "2c248e2d2dba87849c280970a949d140"
build_date: "2019-03-07T20:54:43.898Z"
size_mb: 1755
size: 504995871
sif: "https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/latest/2019-03-07-985eed76-2c248e2d/2c248e2d2dba87849c280970a949d140.simg"
url: https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/latest/2019-03-07-985eed76-2c248e2d/
recipe: https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/latest/2019-03-07-985eed76-2c248e2d/Singularity
collection: tobiasschlatter/BA-Eye-Tracking
---

# tobiasschlatter/BA-Eye-Tracking:latest

```bash
$ singularity pull shub://tobiasschlatter/BA-Eye-Tracking:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%labels
   Maintainer Daniel Wassmer & Tobias Schlatter
   Version v0.1
   
%environment
     conda=/opt/conda/bin/conda
     pip=/opt/conda/bin/pip
     python3=/opt/conda/bin/python
     export conda pip python3
     
%runscript
     echo "Running scripts..."

%post
     
     # Update conda packages
     /opt/conda/bin/conda update --all -y --quiet
     # Install basic packages
     /opt/conda/bin/conda install -c conda-forge -y -q pip matplotlib tqdm jupyter cython scipy numpy pandas tensorflow
     # Update pip
     /opt/conda/bin/pip install -U pip -q
     # Clean up
     /opt/conda/bin/conda clean --all -y --quiet
     apt-get autoremove -y
     apt-get clean

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [tobiasschlatter/BA-Eye-Tracking](https://github.com/tobiasschlatter/BA-Eye-Tracking)
 - License: None

