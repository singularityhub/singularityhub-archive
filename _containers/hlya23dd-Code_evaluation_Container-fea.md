---
id: 14041
name: "hlya23dd/Code_evaluation_Container"
branch: "master"
tag: "fea"
commit: "139f0eda3c47d0b7c0302447b6f09c8fa2e57e3a"
version: "d9d8a7a4a44f2721a0505a9c968077cca17129745ae10516ef830407e061b047"
build_date: "2020-08-24T12:09:56.458Z"
size_mb: 554.7109375
size: 581656576
sif: "https://datasets.datalad.org/shub/hlya23dd/Code_evaluation_Container/fea/2020-08-24-139f0eda-d9d8a7a4/d9d8a7a4a44f2721a0505a9c968077cca17129745ae10516ef830407e061b047.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/hlya23dd/Code_evaluation_Container/fea/2020-08-24-139f0eda-d9d8a7a4/
recipe: https://datasets.datalad.org/shub/hlya23dd/Code_evaluation_Container/fea/2020-08-24-139f0eda-d9d8a7a4/Singularity
collection: hlya23dd/Code_evaluation_Container
---

# hlya23dd/Code_evaluation_Container:fea

```bash
$ singularity pull shub://hlya23dd/Code_evaluation_Container:fea
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.15.2-py3

%labels
    CREATER hlya23dd

%files
    requirements.txt

%post
    pip install -r requirements.txt
```

## Collection

 - Name: [hlya23dd/Code_evaluation_Container](https://github.com/hlya23dd/Code_evaluation_Container)
 - License: [MIT License](https://api.github.com/licenses/mit)

