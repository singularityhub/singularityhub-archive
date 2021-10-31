---
id: 3339
name: "xuzhaoqing/DeepSpeech"
branch: "master"
tag: "latest"
commit: "41bdfb44e68a08507b419090a58de0a8f56c185e"
version: "f84ebe48081a831bf90fd847c589d129"
build_date: "2019-05-30T08:05:55.115Z"
size_mb: 4365
size: 2763235359
sif: "https://datasets.datalad.org/shub/xuzhaoqing/DeepSpeech/latest/2019-05-30-41bdfb44-f84ebe48/f84ebe48081a831bf90fd847c589d129.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/xuzhaoqing/DeepSpeech/latest/2019-05-30-41bdfb44-f84ebe48/
recipe: https://datasets.datalad.org/shub/xuzhaoqing/DeepSpeech/latest/2019-05-30-41bdfb44-f84ebe48/Singularity
collection: xuzhaoqing/DeepSpeech
---

# xuzhaoqing/DeepSpeech:latest

```bash
$ singularity pull shub://xuzhaoqing/DeepSpeech:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:paddlepaddle/deep_speech:latest-gpu

%labels
ARTHUR ZhaoqingXu

%environment
	export LANG='C.UTF-8'
        export HOME="/mnt/rds/redhen/gallina/Singularity"

%post
  apt-get update && apt-get -y install ffmpeg sox
  pip install webrtcvad
```

## Collection

 - Name: [xuzhaoqing/DeepSpeech](https://github.com/xuzhaoqing/DeepSpeech)
 - License: None

