---
id: 3986
name: "sjmielke/singularity-recipes"
branch: "master"
tag: "0.4.1"
commit: "13e47025ad14347e7c5fcefed0bc9448d6a9c813"
version: "6d586da1181e2d4fa8c4935b1fdfd65a"
build_date: "2018-08-15T09:33:42.902Z"
size_mb: 8883
size: 4648853535
sif: "https://datasets.datalad.org/shub/sjmielke/singularity-recipes/0.4.1/2018-08-15-13e47025-6d586da1/6d586da1181e2d4fa8c4935b1fdfd65a.simg"
url: https://datasets.datalad.org/shub/sjmielke/singularity-recipes/0.4.1/2018-08-15-13e47025-6d586da1/
recipe: https://datasets.datalad.org/shub/sjmielke/singularity-recipes/0.4.1/2018-08-15-13e47025-6d586da1/Singularity
collection: sjmielke/singularity-recipes
---

# sjmielke/singularity-recipes:0.4.1

```bash
$ singularity pull shub://sjmielke/singularity-recipes:0.4.1
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

 - Name: [sjmielke/singularity-recipes](https://github.com/sjmielke/singularity-recipes)
 - License: None

