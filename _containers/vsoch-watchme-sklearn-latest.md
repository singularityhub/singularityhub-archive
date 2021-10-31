---
id: 9044
name: "vsoch/watchme-sklearn"
branch: "master"
tag: "latest"
commit: "4411eb6a6ce24a433fcfd8db47b1a8dd7da9b24f"
version: "7851f1274c158ed64a35bfc3e89c3aa1"
build_date: "2020-09-01T14:31:57.177Z"
size_mb: 2635.0
size: 1190821919
sif: "https://datasets.datalad.org/shub/vsoch/watchme-sklearn/latest/2020-09-01-4411eb6a-7851f127/7851f1274c158ed64a35bfc3e89c3aa1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/vsoch/watchme-sklearn/latest/2020-09-01-4411eb6a-7851f127/
recipe: https://datasets.datalad.org/shub/vsoch/watchme-sklearn/latest/2020-09-01-4411eb6a-7851f127/Singularity
collection: vsoch/watchme-sklearn
---

# vsoch/watchme-sklearn:latest

```bash
$ singularity pull shub://vsoch/watchme-sklearn:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%files
    plot_lle_digits.py /plot_lle_digits.py

%post
    apt-get update && apt-get install -y git g++ gcc
    /opt/conda/bin/conda install numpy matplotlib scikit-learn
    git clone -b add/custom-envars https://www.github.com/vsoch/watchme
    cd watchme
    /opt/conda/bin/pip install .[all]

%environment
    WATCHMEENV_LABEL="singularity-container"
    PATH=/opt/conda/bin:$PATH
    export WATCHMEENV_LABEL PATH

%runscript
    watchme create watchme-sklearn
    /opt/conda/bin/python /plot_lle_digits.py
```

## Collection

 - Name: [vsoch/watchme-sklearn](https://github.com/vsoch/watchme-sklearn)
 - License: None

