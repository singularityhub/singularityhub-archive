---
id: 7625
name: "mohanliu/Singularity_data_science_python"
branch: "master"
tag: "latest"
commit: "bbf4a83fbc96122b716cc94a1e72f6ede5b7ee88"
version: "26e451e936d3a6f3ead92200e75c56f3"
build_date: "2019-10-17T14:59:43.655Z"
size_mb: 2595
size: 801910815
sif: "https://datasets.datalad.org/shub/mohanliu/Singularity_data_science_python/latest/2019-10-17-bbf4a83f-26e451e9/26e451e936d3a6f3ead92200e75c56f3.simg"
url: https://datasets.datalad.org/shub/mohanliu/Singularity_data_science_python/latest/2019-10-17-bbf4a83f-26e451e9/
recipe: https://datasets.datalad.org/shub/mohanliu/Singularity_data_science_python/latest/2019-10-17-bbf4a83f-26e451e9/Singularity
collection: mohanliu/Singularity_data_science_python
---

# mohanliu/Singularity_data_science_python:latest

```bash
$ singularity pull shub://mohanliu/Singularity_data_science_python:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%labels
   Maintainer MohanLiu (mohan@u.northwestern.edu)
   Version v0.0
   
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
     # Install conda packages
     /opt/conda/bin/conda install -c conda-forge -y -q pip matplotlib tqdm jupyter cython scipy numpy pandas scikit-learn seaborn lightgbm tensorflow 
     /opt/conda/bin/conda install -c conda-forge -y -q tornado=5.1.1
     # Update pip
     /opt/conda/bin/pip install -U pip -q
     # Install additional packages
     /opt/conda/bin/pip install keras pydot
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

 - Name: [mohanliu/Singularity_data_science_python](https://github.com/mohanliu/Singularity_data_science_python)
 - License: [MIT License](https://api.github.com/licenses/mit)

