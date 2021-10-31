---
id: 8549
name: "Sylvia-Liang/torchstf"
branch: "master"
tag: "latest"
commit: "e5f5831d63732df4930309ee3096cfba9165c32c"
version: "fa422a1131d0a77fdbe64f3d26c2b8c6"
build_date: "2019-04-22T14:00:06.508Z"
size_mb: 9834
size: 5090013215
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torchstf/latest/2019-04-22-e5f5831d-fa422a11/fa422a1131d0a77fdbe64f3d26c2b8c6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torchstf/latest/2019-04-22-e5f5831d-fa422a11/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torchstf/latest/2019-04-22-e5f5831d-fa422a11/Singularity
collection: Sylvia-Liang/torchstf
---

# Sylvia-Liang/torchstf:latest

```bash
$ singularity pull shub://Sylvia-Liang/torchstf:latest
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:marcc-hpc/pytorch

%post
  # Downgrade pytorch
  /opt/conda/bin/pip install torch==0.4.1
  # Reinstall most current tensorbaordX, something magic about pip...
  /opt/conda/bin/conda uninstall tensorboardx
  /opt/conda/bin/pip install -U tensorboardx
  /opt/conda/bin/pip uninstall -y tensorboardx
  /opt/conda/bin/conda install -c conda-forge tensorboardx
  /opt/conda/bin/pip install stanfordnlp
```

## Collection

 - Name: [Sylvia-Liang/torchstf](https://github.com/Sylvia-Liang/torchstf)
 - License: None

