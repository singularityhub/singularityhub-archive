---
id: 8544
name: "Sylvia-Liang/pytorch"
branch: "master"
tag: "latest"
commit: "680cbc63b8458d61ce83714b3e0ebf529250fbc6"
version: "9a5bad6792deb56aa6f5e6199d5dc2de"
build_date: "2019-04-22T14:00:06.494Z"
size_mb: 9833
size: 5089640479
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/pytorch/latest/2019-04-22-680cbc63-9a5bad67/9a5bad6792deb56aa6f5e6199d5dc2de.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/pytorch/latest/2019-04-22-680cbc63-9a5bad67/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/pytorch/latest/2019-04-22-680cbc63-9a5bad67/Singularity
collection: Sylvia-Liang/pytorch
---

# Sylvia-Liang/pytorch:latest

```bash
$ singularity pull shub://Sylvia-Liang/pytorch:latest
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
```

## Collection

 - Name: [Sylvia-Liang/pytorch](https://github.com/Sylvia-Liang/pytorch)
 - License: None

