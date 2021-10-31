---
id: 8779
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "multiqc"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "684ac075821172246b21dd8f3fd07504"
build_date: "2019-05-08T15:11:14.381Z"
size_mb: 1195
size: 450273311
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/multiqc/2019-05-08-5f15386e-684ac075/684ac075821172246b21dd8f3fd07504.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/multiqc/2019-05-08-5f15386e-684ac075/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/multiqc/2019-05-08-5f15386e-684ac075/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:multiqc

```bash
$ singularity pull shub://jlboat/BioinfoContainers:multiqc
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: python:2

%post
    apt-get update --fix-missing && apt-get install -y python-pip
    pip install multiqc

%runscript
    exec multiqc "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

