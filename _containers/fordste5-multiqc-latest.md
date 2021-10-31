---
id: 455
name: "fordste5/multiqc"
branch: "master"
tag: "latest"
commit: "ca9359212d7c2808ecf7bcfdb288d3a0bbd2755f"
version: "1db24d849e49778f4de35dad56cb6abf"
build_date: "2017-10-20T13:38:17.337Z"
size_mb: 1859
size: 770846751
sif: "https://datasets.datalad.org/shub/fordste5/multiqc/latest/2017-10-20-ca935921-1db24d84/1db24d849e49778f4de35dad56cb6abf.simg"
url: https://datasets.datalad.org/shub/fordste5/multiqc/latest/2017-10-20-ca935921-1db24d84/
recipe: https://datasets.datalad.org/shub/fordste5/multiqc/latest/2017-10-20-ca935921-1db24d84/Singularity
collection: fordste5/multiqc
---

# fordste5/multiqc:latest

```bash
$ singularity pull shub://fordste5/multiqc:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/multiqc


%post
mkdir -p /boot
mkdir -p /cvmfs
mkdir -p /mnt/home
mkdir -p /mnt/research
mkdir -p /mnt/dfs17
mkdir -p /mnt/ffs17
mkdir -p /mnt/local
mkdir -p /mnt/ls15
mkdir -p /opt/software
chmod o+r /opt/conda/lib/python2.7/site-packages/.wh.conda-4.3.14-py2.7.egg-info
```

## Collection

 - Name: [fordste5/multiqc](https://github.com/fordste5/multiqc)
 - License: None

