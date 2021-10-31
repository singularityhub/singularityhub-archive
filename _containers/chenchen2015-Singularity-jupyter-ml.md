---
id: 4226
name: "chenchen2015/Singularity-jupyter"
branch: "master"
tag: "ml"
commit: "4e67fdc338c4d1d4e9a8c1b6a920d63139539af8"
version: "60db974bb7d9c92c32569598f228c7e4"
build_date: "2019-03-06T04:56:22.624Z"
size_mb: 2263
size: 770715679
sif: "https://datasets.datalad.org/shub/chenchen2015/Singularity-jupyter/ml/2019-03-06-4e67fdc3-60db974b/60db974bb7d9c92c32569598f228c7e4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/chenchen2015/Singularity-jupyter/ml/2019-03-06-4e67fdc3-60db974b/
recipe: https://datasets.datalad.org/shub/chenchen2015/Singularity-jupyter/ml/2019-03-06-4e67fdc3-60db974b/Singularity
collection: chenchen2015/Singularity-jupyter
---

# chenchen2015/Singularity-jupyter:ml

```bash
$ singularity pull shub://chenchen2015/Singularity-jupyter:ml
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
     /opt/conda/bin/conda install -c conda-forge lightgbm scikit-learn seaborn opencv pillow scikit-image -y -q
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

