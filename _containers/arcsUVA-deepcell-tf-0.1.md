---
id: 9389
name: "arcsUVA/deepcell-tf"
branch: "master"
tag: "0.1"
commit: "4d372711b03583375e4ec8f08cead1891dbffae3"
version: "cad2255fae1a6414263ef2f3fcc93f7c"
build_date: "2019-05-29T07:57:59.258Z"
size_mb: 3841
size: 2091937823
sif: "https://datasets.datalad.org/shub/arcsUVA/deepcell-tf/0.1/2019-05-29-4d372711-cad2255f/cad2255fae1a6414263ef2f3fcc93f7c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arcsUVA/deepcell-tf/0.1/2019-05-29-4d372711-cad2255f/
recipe: https://datasets.datalad.org/shub/arcsUVA/deepcell-tf/0.1/2019-05-29-4d372711-cad2255f/Singularity
collection: arcsUVA/deepcell-tf
---

# arcsUVA/deepcell-tf:0.1

```bash
$ singularity pull shub://arcsUVA/deepcell-tf:0.1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: tensorflow/tensorflow:1.12.0-gpu-py3


%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container

    # mkdir /notebooks/intro_to_tensorflow && \
    # mv BUILD LICENSE /notebooks/*.ipynb intro_to_tensorflow/

    # System maintenance
    apt-get update && apt-get install -y \
        git \
        python3-tk \
        libsm6
        
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip
   
    # get deepcell source code
    cd /opt
    git clone https://github.com/vanvalenlab/deepcell-tf.git
    # update and install requirements
    sed -i 's/tensorflow-gpu==1.11.0/tensorflow-gpu==1.12.0/g' /opt/deepcell-tf/requirements.txt
    pip install -r /opt/deepcell-tf/requirements.txt
    pip install /opt/deepcell-tf
    cd /opt/deepcell-tf
    python setup.py build_ext --inplace

    # Change matplotlibrc file to use the Agg backend
    echo "backend : Agg" > /usr/local/lib/python3.5/dist-packages/matplotlib/mpl-data/matplotlibrc
    

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text code will run whenever the container
# is called as an executable or with `singularity run`
exec python $@


%help
This container is backed by Python 3.5 for:
    * Tensorflow 1.13.1 with Keras implementation
    * DeepCell-TF 0.1


%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
```

## Collection

 - Name: [arcsUVA/deepcell-tf](https://github.com/arcsUVA/deepcell-tf)
 - License: None

