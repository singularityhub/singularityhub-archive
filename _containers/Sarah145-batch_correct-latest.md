---
id: 14160
name: "Sarah145/batch_correct"
branch: "master"
tag: "latest"
commit: "1582b85fd7bcc3053f0c33a139cb22e1ff8ef2aa"
version: "24cdc987c822e9311632b857076d491d"
build_date: "2020-09-07T15:41:37.352Z"
size_mb: 3451.0
size: 1469792287
sif: "https://datasets.datalad.org/shub/Sarah145/batch_correct/latest/2020-09-07-1582b85f-24cdc987/24cdc987c822e9311632b857076d491d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Sarah145/batch_correct/latest/2020-09-07-1582b85f-24cdc987/
recipe: https://datasets.datalad.org/shub/Sarah145/batch_correct/latest/2020-09-07-1582b85f-24cdc987/Singularity
collection: Sarah145/batch_correct
---

# Sarah145/batch_correct:latest

```bash
$ singularity pull shub://Sarah145/batch_correct:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: sarah145/batch_correct:latest
IncludeCmd: yes

%post

    chmod -R o+rX /opt/conda/lib/python3.7/site-packages/*
```

## Collection

 - Name: [Sarah145/batch_correct](https://github.com/Sarah145/batch_correct)
 - License: None

