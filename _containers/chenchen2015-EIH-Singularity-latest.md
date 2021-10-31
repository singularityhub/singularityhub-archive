---
id: 4687
name: "chenchen2015/EIH-Singularity"
branch: "master"
tag: "latest"
commit: "44b9bb14ee785c1f7e22a767e6593ef5dc272153"
version: "7c86bdbb6239ab6163517b6160cca5a2"
build_date: "2019-02-12T21:37:56.920Z"
size_mb: 2751
size: 1058934815
sif: "https://datasets.datalad.org/shub/chenchen2015/EIH-Singularity/latest/2019-02-12-44b9bb14-7c86bdbb/7c86bdbb6239ab6163517b6160cca5a2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/chenchen2015/EIH-Singularity/latest/2019-02-12-44b9bb14-7c86bdbb/
recipe: https://datasets.datalad.org/shub/chenchen2015/EIH-Singularity/latest/2019-02-12-44b9bb14-7c86bdbb/Singularity
collection: chenchen2015/EIH-Singularity
---

# chenchen2015/EIH-Singularity:latest

```bash
$ singularity pull shub://chenchen2015/EIH-Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: chenchen2015/Singularity-jupyter

%help
    This is a Singularity container for EIH simulations.
    It has all the necessarities for reproducing simulation results published in the EIH paper.
    The container by itself is also a minimal Jupyter Notebook server running on Ubuntu with all the libraries required for research computing.

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
     echo "Open browser to localhost:8888 and copy the token below to authenticate"
     exec /opt/conda/bin/jupyter notebook --notebook-dir=/EIH --ip='*' --allow-root --port=8888 --no-browser

%post   
     # Lock version, used to be scipy=1.0.1 numpy=1.14.3
     /opt/conda/bin/conda install -c conda-forge scipy=1.2.0 numpy=1.16.1 -y -qq
     # Install system packages and other dependencies
     /opt/conda/bin/conda install -c conda-forge cython numba -y -qq
     apt-get update
     apt-get install gcc-6 g++-6 libc6-dev gcc g++ -y
     # Clean up
     /opt/conda/bin/conda clean --all -y --quiet
     apt-get autoremove -y
     apt-get clean
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
     # Create bind points for HPCC environment
     mkdir -p /EIH/home

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [chenchen2015/EIH-Singularity](https://github.com/chenchen2015/EIH-Singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

