---
id: 14552
name: "shwertt/neurovista_evaluation_sw"
branch: "main"
tag: "nv_eval"
commit: "60621429658246272951fbd91cd99969cf8d8a02"
version: "6c56b69861853b4aff553d0733762ccb6318e38e7f26c0517044df16e3e3b60d"
build_date: "2020-10-07T08:00:14.383Z"
size_mb: 1699.8203125
size: 1782390784
sif: "https://datasets.datalad.org/shub/shwertt/neurovista_evaluation_sw/nv_eval/2020-10-07-60621429-6c56b698/6c56b69861853b4aff553d0733762ccb6318e38e7f26c0517044df16e3e3b60d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/shwertt/neurovista_evaluation_sw/nv_eval/2020-10-07-60621429-6c56b698/
recipe: https://datasets.datalad.org/shub/shwertt/neurovista_evaluation_sw/nv_eval/2020-10-07-60621429-6c56b698/Singularity
collection: shwertt/neurovista_evaluation_sw
---

# shwertt/neurovista_evaluation_sw:nv_eval

```bash
$ singularity pull shub://shwertt/neurovista_evaluation_sw:nv_eval
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:2.0.1-gpu-py3

%labels
    CREATOR shwertt

%files
    requirements.txt

%post
    pip install -r requirements.txt
```

## Collection

 - Name: [shwertt/neurovista_evaluation_sw](https://github.com/shwertt/neurovista_evaluation_sw)
 - License: [MIT License](https://api.github.com/licenses/mit)

