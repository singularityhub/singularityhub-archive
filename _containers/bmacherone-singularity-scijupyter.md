---
id: 9601
name: "bmacherone/singularity"
branch: "master"
tag: "scijupyter"
commit: "2ce967c1f1d8b55cc2d7e687656f1cc77e288a97"
version: "ca76e4fc7b77e9e96bc25b159a782760"
build_date: "2019-06-08T01:44:30.058Z"
size_mb: 9499
size: 4276944927
sif: "https://datasets.datalad.org/shub/bmacherone/singularity/scijupyter/2019-06-08-2ce967c1-ca76e4fc/ca76e4fc7b77e9e96bc25b159a782760.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bmacherone/singularity/scijupyter/2019-06-08-2ce967c1-ca76e4fc/
recipe: https://datasets.datalad.org/shub/bmacherone/singularity/scijupyter/2019-06-08-2ce967c1-ca76e4fc/Singularity
collection: bmacherone/singularity
---

# bmacherone/singularity:scijupyter

```bash
$ singularity pull shub://bmacherone/singularity:scijupyter
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
description "A scientific python environment with Jupyter notebook interface"
maintainer "Brian Macherone <bmacherone@albany.edu>"
version "0.1 beta"

# Set environment variables
%environment
export LANG=C.UTF-8 LC_ALL=C.UTF-8
export PATH=/opt/conda/bin:$PATH

%post
export PATH=/opt/conda/bin:$PATH

# install Ubuntu packages
apt-get update
apt-get install -y \
    wget \
    ca-certificates \
    git-core \
    pkg-config \
    tree \
    tcsh \
    apcalc \
    freetds-dev

# clean up
apt-get clean 
rm -rf /var/lib/apt/lists/* 

# Install Jupyter config
# some prep for git to access github.com
#mkdir ~/.ssh && touch ~/.ssh/known_hosts 
#ssh-keygen -F github.com || ssh-keyscan github.com >> ~/.ssh/known_hosts 
# get configuration files from b lindesy, only use jupyter stuff
#git clone https://github.com/bobbywlindsey/dotfiles.git 
mkdir ~/.jupyter 
mkdir -p ~/.jupyter/custom 
mkdir -p ~/.jupyter/nbconfig 
#cp /dotfiles/jupyter/jupyter_notebook_config.py ~/.jupyter/ 
wget https://raw.githubusercontent.com/bmacherone/singularity/master/jupyter_notebook_config.py \
    -O ~/.jupyter/jupyter_notebook_config.py
#cp /dotfiles/jupyter/custom/custom.js ~/.jupyter/custom/ 
wget https://raw.githubusercontent.com/bmacherone/singularity/master/custom.js \
    -O ~/.jupyter/custom/custom.js
#cp /dotfiles/jupyter/nbconfig/notebook.json ~/.jupyter/nbconfig/ 
wget https://raw.githubusercontent.com/bmacherone/singularity/master/notebook.json \
    -O ~/.jupyter/nbconfig/notebook.json
#rm -rf /dotfiles 

# Install Anaconda
echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh 
wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh 
/bin/bash ~/anaconda.sh -b -p /opt/conda 
rm ~/anaconda.sh 

# Update Anaconda
conda update conda 
conda update anaconda 
conda update --all 

# Install Jupyter theme
pip install msgpack jupyterthemes 
jt -t grade3 

# Install 
# Install other Python packages
conda install pymssql mkl=2018 
pip install SQLAlchemy \
missingno \
json_tricks \
bcolz \
gensim \
elasticsearch \
psycopg2-binary \
jupyter_contrib_nbextensions \
jupyter_nbextensions_configurator \
pymc3 

# Enable Jupyter Notebook extensions
jupyter contrib nbextension install --user 
jupyter nbextensions_configurator enable --user 
jupyter nbextension enable codefolding/main 
jupyter nbextension enable collapsible_headings/main 

# Add vim-binding extension
mkdir -p $(jupyter --data-dir)/nbextensions 
git clone https://github.com/lambdalisue/jupyter-vim-binding $(jupyter --data-dir)/nbextensions/vim_binding 
cd $(jupyter --data-dir)/nbextensions
chmod -R go-w vim_binding 

# remove everything you don't need
apt-get remove -y wget git-core pkg-config


%runscript
export XDG_RUNTIME_DIR=""
cd ~/notebooks
jupyter lab --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='data-science'


%test
grep -q NAME=\"Ubuntu\" /etc/os-release
if [ $? -eq 0 ]; then
echo "Container base is Ubuntu as expected."
else
echo "Container base is not Ubuntu."
fi
```

## Collection

 - Name: [bmacherone/singularity](https://github.com/bmacherone/singularity)
 - License: None

