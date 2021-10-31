---
id: 3348
name: "xuzhaoqing/DeepSpeech"
branch: "master"
tag: "xu"
commit: "b0a06b55d3d1844753aed74d1d3312151a343681"
version: "bb085ebfe89971809bdb5846fd4f8686"
build_date: "2018-09-24T07:21:05.041Z"
size_mb: 4175
size: 2685673503
sif: "https://datasets.datalad.org/shub/xuzhaoqing/DeepSpeech/xu/2018-09-24-b0a06b55-bb085ebf/bb085ebfe89971809bdb5846fd4f8686.simg"
url: https://datasets.datalad.org/shub/xuzhaoqing/DeepSpeech/xu/2018-09-24-b0a06b55-bb085ebf/
recipe: https://datasets.datalad.org/shub/xuzhaoqing/DeepSpeech/xu/2018-09-24-b0a06b55-bb085ebf/Singularity
collection: xuzhaoqing/DeepSpeech
---

# xuzhaoqing/DeepSpeech:xu

```bash
$ singularity pull shub://xuzhaoqing/DeepSpeech:xu
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:paddlepaddle/deep_speech:latest-gpu

%labels
ARTHUR Zhaoqing Xu

%environment
	export LANGUAGE="zh_CN:zh:en_US:en"
	export LANG="zh_CN.UTF-8"
	export HOME="/mnt/rds/redhen/gallina/Singularity"
```

## Collection

 - Name: [xuzhaoqing/DeepSpeech](https://github.com/xuzhaoqing/DeepSpeech)
 - License: None

