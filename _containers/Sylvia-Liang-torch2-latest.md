---
id: 8553
name: "Sylvia-Liang/torch2"
branch: "master"
tag: "latest"
commit: "9fb48aab0fdbdf091bd1b99f4ade55aaf98557af"
version: "6588b5d51fff54584f1d5614361cc9f3"
build_date: "2019-04-22T21:53:08.837Z"
size_mb: 11676
size: 6557208607
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch2/latest/2019-04-22-9fb48aab-6588b5d5/6588b5d51fff54584f1d5614361cc9f3.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/torch2/latest/2019-04-22-9fb48aab-6588b5d5/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch2/latest/2019-04-22-9fb48aab-6588b5d5/Singularity
collection: Sylvia-Liang/torch2
---

# Sylvia-Liang/torch2:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch2:latest
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
  /opt/conda/bin/pip install nltk
  /opt/conda/bin/pip install sparqlwrapper
  /opt/conda/bin/pip install tqdm
  /opt/conda/bin/conda install -c maciejkula -c pytorch spotlight=0.1.5
  /opt/conda/bin/pip install inflect
  /opt/conda/bin/pip install tagme
  /opt/conda/bin/pip install git+https://github.com/facebookresearch/fastText.git
```

## Collection

 - Name: [Sylvia-Liang/torch2](https://github.com/Sylvia-Liang/torch2)
 - License: None

