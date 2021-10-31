---
id: 2414
name: "davidinouye/singularity"
branch: "master"
tag: "latest"
commit: "c4021d3b26310b3903625b5d827e4e41bfbf24ab"
version: "52a536c2567b4059693a5d356e192e70"
build_date: "2018-04-05T16:53:47.976Z"
size_mb: 6913
size: 2602864671
sif: "https://datasets.datalad.org/shub/davidinouye/singularity/latest/2018-04-05-c4021d3b-52a536c2/52a536c2567b4059693a5d356e192e70.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/davidinouye/singularity/latest/2018-04-05-c4021d3b-52a536c2/
recipe: https://datasets.datalad.org/shub/davidinouye/singularity/latest/2018-04-05-c4021d3b-52a536c2/Singularity
collection: davidinouye/singularity
---

# davidinouye/singularity:latest

```bash
$ singularity pull shub://davidinouye/singularity:latest
```

## Singularity Recipe

```singularity
#!/bin/sh
Bootstrap: docker
From: davidinouye/research

%help
This just builds a singularity image based on a docker image.

%labels
Version v0.2
```

## Collection

 - Name: [davidinouye/singularity](https://github.com/davidinouye/singularity)
 - License: None

