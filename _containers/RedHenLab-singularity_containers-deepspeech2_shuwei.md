---
id: 3476
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "deepspeech2_shuwei"
commit: "9173cce65ce84351ce9ee186c5849fd0e339b270"
version: "97aaecdf98bc727e7b39dcddf32e0540"
build_date: "2018-07-13T21:19:59.406Z"
size_mb: 4175
size: 2685673503
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2_shuwei/2018-07-13-9173cce6-97aaecdf/97aaecdf98bc727e7b39dcddf32e0540.simg"
url: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2_shuwei/2018-07-13-9173cce6-97aaecdf/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/deepspeech2_shuwei/2018-07-13-9173cce6-97aaecdf/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:deepspeech2_shuwei

```bash
$ singularity pull shub://RedHenLab/singularity_containers:deepspeech2_shuwei
```

## Singularity Recipe

```singularity
Bootstrap:docker 
From:paddlepaddle/deep_speech:latest-gpu

%labels
        MAINTAINER Shuwei Xu

%environment
        unset HOME
        export HOME="/mnt/rds/redhen/gallina/Singularity/DeepSpeech2/DeepSpeech"
        export GST_ID3_TAG_ENCODING=GB2312

%post
```

## Collection

 - Name: [RedHenLab/singularity_containers](https://github.com/RedHenLab/singularity_containers)
 - License: None

