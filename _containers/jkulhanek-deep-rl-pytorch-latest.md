---
id: 7877
name: "jkulhanek/deep-rl-pytorch"
branch: "master"
tag: "latest"
commit: "8678d7d6ff1f4653ee90a61f0097264a0c9f68e6"
version: "74033851c393f63c70aba410737a7bcd"
build_date: "2020-05-12T16:39:22.808Z"
size_mb: 5541
size: 3440877599
sif: "https://datasets.datalad.org/shub/jkulhanek/deep-rl-pytorch/latest/2020-05-12-8678d7d6-74033851/74033851c393f63c70aba410737a7bcd.simg"
url: https://datasets.datalad.org/shub/jkulhanek/deep-rl-pytorch/latest/2020-05-12-8678d7d6-74033851/
recipe: https://datasets.datalad.org/shub/jkulhanek/deep-rl-pytorch/latest/2020-05-12-8678d7d6-74033851/Singularity
collection: jkulhanek/deep-rl-pytorch
---

# jkulhanek/deep-rl-pytorch:latest

```bash
$ singularity pull shub://jkulhanek/deep-rl-pytorch:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: kulhanek/deep-rl-pytorch:latest


%post
    mkdir /deep-rl-pytorch
    cd /deep-rl-pytorch
    git init
    git remote add origin https://github.com/jkulhanek/deep-rl-pytorch.git
    git pull origin master

%runscript
    echo "Container is ready!"
    echo "Launching experiment with arguments [$@]"
    exec python3 "/deep-rl-pytorch/$@"
```

## Collection

 - Name: [jkulhanek/deep-rl-pytorch](https://github.com/jkulhanek/deep-rl-pytorch)
 - License: [MIT License](https://api.github.com/licenses/mit)

