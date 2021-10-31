---
id: 4101
name: "marcc-hpc/pytorch"
branch: "0.5.0"
tag: "0.4.1"
commit: "17ea6c57beec35acb01d7553f29928a7adb9f563"
version: "84476d7bef7546af8d824367bf6024c8"
build_date: "2019-12-16T13:31:28.547Z"
size_mb: 8889
size: 4649934879
sif: "https://datasets.datalad.org/shub/marcc-hpc/pytorch/0.4.1/2019-12-16-17ea6c57-84476d7b/84476d7bef7546af8d824367bf6024c8.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/pytorch/0.4.1/2019-12-16-17ea6c57-84476d7b/
recipe: https://datasets.datalad.org/shub/marcc-hpc/pytorch/0.4.1/2019-12-16-17ea6c57-84476d7b/Singularity
collection: marcc-hpc/pytorch
---

# marcc-hpc/pytorch:0.4.1

```bash
$ singularity pull shub://marcc-hpc/pytorch:0.4.1
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

 - Name: [marcc-hpc/pytorch](https://github.com/marcc-hpc/pytorch)
 - License: [MIT License](https://api.github.com/licenses/mit)

