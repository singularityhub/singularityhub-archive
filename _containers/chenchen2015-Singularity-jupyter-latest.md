---
id: 4005
name: "chenchen2015/Singularity-jupyter"
branch: "master"
tag: "latest"
commit: "f1cf1b3c8b409a283e9a8870158690b92d7a84eb"
version: "7dc17c56fadcd68b52f8669a50ee4505"
build_date: "2021-02-21T10:55:09.255Z"
size_mb: 1400
size: 437252127
sif: "https://datasets.datalad.org/shub/chenchen2015/Singularity-jupyter/latest/2021-02-21-f1cf1b3c-7dc17c56/7dc17c56fadcd68b52f8669a50ee4505.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/chenchen2015/Singularity-jupyter/latest/2021-02-21-f1cf1b3c-7dc17c56/
recipe: https://datasets.datalad.org/shub/chenchen2015/Singularity-jupyter/latest/2021-02-21-f1cf1b3c-7dc17c56/Singularity
collection: chenchen2015/Singularity-jupyter
---

# chenchen2015/Singularity-jupyter:latest

```bash
$ singularity pull shub://chenchen2015/Singularity-jupyter:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%labels
   Maintainer Chen Chen (chenchen.bme@gmail.com)
   Version v0.2
   
%environment
     conda=/opt/conda/bin/conda
     pip=/opt/conda/bin/pip
     python3=/opt/conda/bin/python
     export conda pip python3
     
%runscript
     echo "Starting notebook..."
     echo "Open browser to localhost:8888"
     exec /opt/conda/bin/jupyter notebook --notebook-dir=/projects --allow-root --port=8888 --no-browser

%post   
     # Update conda packages
     /opt/conda/bin/conda update --all -y --quiet
     # Install basic packages
     /opt/conda/bin/conda install -c conda-forge -y -q pip matplotlib tqdm jupyter cython scipy numpy pandas
     # Update pip
     /opt/conda/bin/pip install -U pip -q
     # Clean up
     /opt/conda/bin/conda clean --all -y --quiet
     apt-get autoremove -y
     apt-get clean
     # create bind points for HPCC environment
     mkdir -p /projects

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [chenchen2015/Singularity-jupyter](https://github.com/chenchen2015/Singularity-jupyter)
 - License: [Other](None)

