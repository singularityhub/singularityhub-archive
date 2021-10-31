---
id: 8646
name: "Sylvia-Liang/torch21"
branch: "master"
tag: "latest"
commit: "50545a4d2fcc44f5fea96f2835f633f8a3e9fa94"
version: "d4bc6c94a518b2207e0fc15caf260af5"
build_date: "2019-04-25T15:46:05.833Z"
size_mb: 10633
size: 5817159711
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch21/latest/2019-04-25-50545a4d-d4bc6c94/d4bc6c94a518b2207e0fc15caf260af5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch21/latest/2019-04-25-50545a4d-d4bc6c94/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch21/latest/2019-04-25-50545a4d-d4bc6c94/Singularity
collection: Sylvia-Liang/torch21
---

# Sylvia-Liang/torch21:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch21:latest
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
  /opt/conda/bin/pip install inflect
  /opt/conda/bin/pip install tagme
  /opt/conda/bin/pip install gensim
  /opt/conda/bin/pip install git+https://github.com/facebookresearch/fastText.git
```

## Collection

 - Name: [Sylvia-Liang/torch21](https://github.com/Sylvia-Liang/torch21)
 - License: None

