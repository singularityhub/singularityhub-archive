---
id: 12189
name: "RickGelhausen/deepribo_image"
branch: "master"
tag: "latest"
commit: "949e8b129bff073142217927bfe372370efc187a"
version: "9bef69eb55fe28de63ba5300a521e1a5"
build_date: "2020-02-06T09:43:39.509Z"
size_mb: 3519.0
size: 1595944991
sif: "https://datasets.datalad.org/shub/RickGelhausen/deepribo_image/latest/2020-02-06-949e8b12-9bef69eb/9bef69eb55fe28de63ba5300a521e1a5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/RickGelhausen/deepribo_image/latest/2020-02-06-949e8b12-9bef69eb/
recipe: https://datasets.datalad.org/shub/RickGelhausen/deepribo_image/latest/2020-02-06-949e8b12-9bef69eb/Singularity
collection: RickGelhausen/deepribo_image
---

# RickGelhausen/deepribo_image:latest

```bash
$ singularity pull shub://RickGelhausen/deepribo_image:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%environment
    ## ensure deepribo env is in the path variable
    PATH="/home/miniconda3/envs/deepribo/bin:$PATH"

%files
    ## fetch deepribo dependencies
    deepribo.yaml

%post
    ## install wget and unzip
    apt-get update && apt-get install -y wget && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

    ## install conda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/miniconda.sh
    bash /home/miniconda.sh -b -p /home/miniconda3
    rm /home/miniconda.sh
    export PATH="/home/miniconda3/bin:${PATH}"

    ## update conda
    conda --version
    conda update -n base -c defaults conda
    conda --version

    ## create conda env and ensure that it runs on startup
    conda env create --file deepribo.yaml
    echo "source activate deepribo" > ~/.bashrc
    export PATH="/home/miniconda3/envs/deepribo/bin:$PATH"

    ## install r
    conda install -c conda-forge r-base r-sizer r-optparse

    ## download DeepRibo
    wget https://github.com/Biobix/DeepRibo/archive/master.zip
    unzip master.zip -d /home && rm master.zip

    ## add shebang and fix minor issues with DeepRibo
    sed -i '1 i\#!/usr/bin/env python' /home/DeepRibo-master/src/*.py
    sed -i '1 i\#!/usr/bin/env Rscript' /home/DeepRibo-master/src/*.R
    sed -i 's/model.load_state_dict(torch.load(model_name, map_location=device))/model.load_state_dict(torch.load(model_name, map_location=device),strict=False)/g' /home/DeepRibo-master/src/DeepRibo.py
    sed -i 's/sys.exit(ParseArgs())/ParseArgs()/g' /home/DeepRibo-master/src/DeepRibo.py

    ## cleaning up
    cp /home/DeepRibo-master/src/*.py /usr/local/bin && cp /home/DeepRibo-master/src/*.R /usr/local/bin && rm -rf /home/DeepRibo-master/

    ## make files executable
    chmod +x /usr/local/bin/DataParser.py
    chmod +x /usr/local/bin/DeepRibo.py
    chmod +x /usr/local/bin/PredictToBedgraph.py
    chmod +x /usr/local/bin/s_curve_cutoff_estimation.R

    ## test deepribo commands
    DeepRibo.py -h
    DataParser.py -h
    PredictToBedgraph.py -h
    s_curve_cutoff_estimation.R

%runscript
    exec "$@"
```

## Collection

 - Name: [RickGelhausen/deepribo_image](https://github.com/RickGelhausen/deepribo_image)
 - License: None

