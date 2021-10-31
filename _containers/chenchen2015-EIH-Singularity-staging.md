---
id: 7165
name: "chenchen2015/EIH-Singularity"
branch: "master"
tag: "staging"
commit: "d74f3c3cc14b4d1fba7241ede57e4ea6a27099ca"
version: "75022568c32a7e1504022a52f9729abe"
build_date: "2019-02-15T00:23:13.027Z"
size_mb: 1978
size: 782852127
sif: "https://datasets.datalad.org/shub/chenchen2015/EIH-Singularity/staging/2019-02-15-d74f3c3c-75022568/75022568c32a7e1504022a52f9729abe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/chenchen2015/EIH-Singularity/staging/2019-02-15-d74f3c3c-75022568/
recipe: https://datasets.datalad.org/shub/chenchen2015/EIH-Singularity/staging/2019-02-15-d74f3c3c-75022568/Singularity
collection: chenchen2015/EIH-Singularity
---

# chenchen2015/EIH-Singularity:staging

```bash
$ singularity pull shub://chenchen2015/EIH-Singularity:staging
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%help
    This is a Singularity container for EIH simulations (Staging repo).
    It has all the necessarities for reproducing simulation results published in the EIH paper.
    The container by itself is also a minimal Jupyter Notebook server running on Ubuntu with all the libraries required for research computing.

%labels
    Maintainer Chen Chen (chenchen.bme@gmail.com)
    Version v0.2
   
%environment
     export conda=/opt/conda/bin/conda
     export pip=/opt/conda/bin/pip
     export python3=/opt/conda/bin/python
     
%runscript
     echo "Starting notebook..."
     echo "Open browser to localhost:8888 and copy the token below to authenticate"
     exec /opt/conda/bin/jupyter notebook --notebook-dir=/EIH --ip='*' --allow-root --port=8888 --no-browser

%post 
     # update system and install gcc
     apt-get update
     apt-get install gcc g++ -y
     # update conda
     /opt/conda/bin/conda update --all -y --quiet
     # Update pip
     /opt/conda/bin/pip install -U pip -q
     # Install dependencies
     /opt/conda/bin/conda install -c conda-forge -y -q matplotlib tqdm jupyter cython numba scipy=1.0.1 numpy=1.16.1 
     # Clean up
     /opt/conda/bin/conda clean --all -y --quiet
     apt-get autoremove -y
     apt-get clean
     # create bind points for HPCC environment
     mkdir -p /projects
     # Clone the EIH repository
     mkdir -p /EIH
     cd /EIH
     git clone https://github.com/MacIver-Lab/Ergodic-Information-Harvesting
     cd ./Ergodic-Information-Harvesting/
     git pull
     # Compile Cython codes
     cd ./SimulationCode/ErgodicHarvestingLib/
     /opt/conda/bin/python ./CythonSetup.py build_ext --inplace
     cd ../../Production-Figure-Code/FigureCode/sm-fig4/ErgodicInfotaxisAPI
     /opt/conda/bin/python ./CythonSetup.py build_ext --inplace

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [chenchen2015/EIH-Singularity](https://github.com/chenchen2015/EIH-Singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

