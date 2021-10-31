---
id: 5216
name: "chenchen2015/Singularity-jupyter"
branch: "master"
tag: "dl"
commit: "fcc490388dbdcd416e09453f47adf9c7dd13e8bd"
version: "5c18db6124cf987dd4e9c20d2931c577"
build_date: "2019-03-06T04:56:22.631Z"
size_mb: 3174
size: 1028005919
sif: "https://datasets.datalad.org/shub/chenchen2015/Singularity-jupyter/dl/2019-03-06-fcc49038-5c18db61/5c18db6124cf987dd4e9c20d2931c577.simg"
url: https://datasets.datalad.org/shub/chenchen2015/Singularity-jupyter/dl/2019-03-06-fcc49038-5c18db61/
recipe: https://datasets.datalad.org/shub/chenchen2015/Singularity-jupyter/dl/2019-03-06-fcc49038-5c18db61/Singularity
collection: chenchen2015/Singularity-jupyter
---

# chenchen2015/Singularity-jupyter:dl

```bash
$ singularity pull shub://chenchen2015/Singularity-jupyter:dl
```

## Singularity Recipe

```singularity
BootStrap: shub
From: chenchen2015/Singularity-jupyter

%labels
   Maintainer Chen Chen (chenchen.bme@gmail.com)
   Version v0.1
   
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
     # Install additional packages
     /opt/conda/bin/conda install -c conda-forge lightgbm scikit-learn seaborn opencv pillow scikit-image tensorflow tqdm -y -q
     /opt/conda/bin/conda install -c lukepfister pycuda 
     /opt/conda/bin/pip install -U imutils -q
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

