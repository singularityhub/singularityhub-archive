---
id: 15231
name: "tpall/geo-htseq-paper"
branch: "master"
tag: "latest"
commit: "fff0637b98c8ada5fa6a7edb624cbc84c30f468f"
version: "64fa911839ae337025c4d85554cbc39e"
build_date: "2021-01-26T17:22:22.124Z"
size_mb: 3100.0
size: 1083830303
sif: "https://datasets.datalad.org/shub/tpall/geo-htseq-paper/latest/2021-01-26-fff0637b-64fa9118/64fa911839ae337025c4d85554cbc39e.sif"
url: https://datasets.datalad.org/shub/tpall/geo-htseq-paper/latest/2021-01-26-fff0637b-64fa9118/
recipe: https://datasets.datalad.org/shub/tpall/geo-htseq-paper/latest/2021-01-26-fff0637b-64fa9118/Singularity
collection: tpall/geo-htseq-paper
---

# tpall/geo-htseq-paper:latest

```bash
$ singularity pull shub://tpall/geo-htseq-paper:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: rstatstartu/rstanverse:latest

%labels
  Maintainer tpall

%help
  This will run R packages to fit stan models

%post
  cd / \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [tpall/geo-htseq-paper](https://github.com/tpall/geo-htseq-paper)
 - License: None

