---
id: 8642
name: "Sylvia-Liang/torch18"
branch: "master"
tag: "latest"
commit: "115129ffc94f8f373ce6a4e183cd5b4d651aa281"
version: "182ffdcfe77b0bec9bb9d82c6adaf792"
build_date: "2019-04-25T15:46:05.814Z"
size_mb: 12565
size: 7299641375
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch18/latest/2019-04-25-115129ff-182ffdcf/182ffdcfe77b0bec9bb9d82c6adaf792.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/torch18/latest/2019-04-25-115129ff-182ffdcf/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch18/latest/2019-04-25-115129ff-182ffdcf/Singularity
collection: Sylvia-Liang/torch18
---

# Sylvia-Liang/torch18:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch18:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: marcc-hpc/pytorch

%post
  # Downgrade pytorch
  /opt/conda/bin/pip install torch==0.4.1
  # Reinstall most current tensorbaordX, something magic about pip...
  /opt/conda/bin/conda uninstall tensorboardx
  /opt/conda/bin/pip install -U tensorboardx
  /opt/conda/bin/pip uninstall -y tensorboardx
  /opt/conda/bin/conda install -c conda-forge tensorboardx
  /opt/conda/bin/pip install -I stanfordnlp==0.1.2
  /opt/conda/bin/pip install nltk
  /opt/conda/bin/pip install sparqlwrapper
  /opt/conda/bin/pip install tqdm
  /opt/conda/bin/conda install -c maciejkula -c pytorch spotlight=0.1.5
  /opt/conda/bin/pip install inflect
  /opt/conda/bin/pip install tagme
  /opt/conda/bin/pip install git+https://github.com/facebookresearch/fastText.git
```

## Collection

 - Name: [Sylvia-Liang/torch18](https://github.com/Sylvia-Liang/torch18)
 - License: None

