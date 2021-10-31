---
id: 487
name: "DoaneAS/NGI-ChIPseq"
branch: "master"
tag: "latest"
commit: "7091ba00dceb3c57af629a2bb9d071c089e94fd2"
version: "0905a64f04ded6fff81cb550660c2025"
build_date: "2018-05-11T07:59:58.275Z"
size_mb: 5095
size: 2654851103
sif: "https://datasets.datalad.org/shub/DoaneAS/NGI-ChIPseq/latest/2018-05-11-7091ba00-0905a64f/0905a64f04ded6fff81cb550660c2025.simg"
url: https://datasets.datalad.org/shub/DoaneAS/NGI-ChIPseq/latest/2018-05-11-7091ba00-0905a64f/
recipe: https://datasets.datalad.org/shub/DoaneAS/NGI-ChIPseq/latest/2018-05-11-7091ba00-0905a64f/Singularity
collection: DoaneAS/NGI-ChIPseq
---

# DoaneAS/NGI-ChIPseq:latest

```bash
$ singularity pull shub://DoaneAS/NGI-ChIPseq:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: scilifelab/ngi-chipseq:latest

%post
    mkdir -p /athena
    echo "All Set!"
```

## Collection

 - Name: [DoaneAS/NGI-ChIPseq](https://github.com/DoaneAS/NGI-ChIPseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

