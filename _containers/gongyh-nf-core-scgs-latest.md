---
id: 13527
name: "gongyh/nf-core-scgs"
branch: "master"
tag: "latest"
commit: "f5923314583c777ec4b101c43876ca280082e3e2"
version: "157e92808bee4f8e76035d56be1ab9737032facce7ed4770ecd317bec05d4fdb"
build_date: "2020-10-13T16:10:18.856Z"
size_mb: 3820.265625
size: 4005838848
sif: "https://datasets.datalad.org/shub/gongyh/nf-core-scgs/latest/2020-10-13-f5923314-157e9280/157e92808bee4f8e76035d56be1ab9737032facce7ed4770ecd317bec05d4fdb.sif"
url: https://datasets.datalad.org/shub/gongyh/nf-core-scgs/latest/2020-10-13-f5923314-157e9280/
recipe: https://datasets.datalad.org/shub/gongyh/nf-core-scgs/latest/2020-10-13-f5923314-157e9280/Singularity
collection: gongyh/nf-core-scgs
---

# gongyh/nf-core-scgs:latest

```bash
$ singularity pull shub://gongyh/nf-core-scgs:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: gongyh/scgs:latest
IncludeCmd: yes

%help
    Singularity container for gongyh/scgs pipeline.

%labels
    Author gongyh@qibebt.ac.cn

%runscript
    exec /bin/bash
```

## Collection

 - Name: [gongyh/nf-core-scgs](https://github.com/gongyh/nf-core-scgs)
 - License: [MIT License](https://api.github.com/licenses/mit)

