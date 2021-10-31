---
id: 8623
name: "shaheenkdr/IndianASR"
branch: "master"
tag: "paddle_deepspeech"
commit: "8bb186cc22dda44c9b49b881f1c053d950eeae39"
version: "a689b8b0b31ebdd55a3d16ad32818382"
build_date: "2019-04-24T14:27:17.551Z"
size_mb: 4177
size: 2687012895
sif: "https://datasets.datalad.org/shub/shaheenkdr/IndianASR/paddle_deepspeech/2019-04-24-8bb186cc-a689b8b0/a689b8b0b31ebdd55a3d16ad32818382.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shaheenkdr/IndianASR/paddle_deepspeech/2019-04-24-8bb186cc-a689b8b0/
recipe: https://datasets.datalad.org/shub/shaheenkdr/IndianASR/paddle_deepspeech/2019-04-24-8bb186cc-a689b8b0/Singularity
collection: shaheenkdr/IndianASR
---

# shaheenkdr/IndianASR:paddle_deepspeech

```bash
$ singularity pull shub://shaheenkdr/IndianASR:paddle_deepspeech
```

## Singularity Recipe

```singularity
Bootstrap:docker 
From:paddlepaddle/deep_speech:latest-gpu

%labels
        MAINTAINER Shuwei Xu

%environment
        unset HOME
        export HOME="/mnt/rds/redhen/gallina/home/sxk1497/chinese/DeepSpeech"
        export GST_ID3_TAG_ENCODING=GB2312

%post
        git clone https://github.com/PaddlePaddle/DeepSpeech.git
        cd DeepSpeech
        sh setup.sh
```

## Collection

 - Name: [shaheenkdr/IndianASR](https://github.com/shaheenkdr/IndianASR)
 - License: None

