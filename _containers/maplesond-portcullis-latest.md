---
id: 5070
name: "maplesond/portcullis"
branch: "master"
tag: "latest"
commit: "5b1fc7beb0d7e6a5ac66f95ad22045bcbcc0ea25"
version: "62f62b937d5474c8eff0531613d391b7"
build_date: "2021-02-04T20:15:36.361Z"
size_mb: 1801.0
size: 593403935
sif: "https://datasets.datalad.org/shub/maplesond/portcullis/latest/2021-02-04-5b1fc7be-62f62b93/62f62b937d5474c8eff0531613d391b7.sif"
url: https://datasets.datalad.org/shub/maplesond/portcullis/latest/2021-02-04-5b1fc7be-62f62b93/
recipe: https://datasets.datalad.org/shub/maplesond/portcullis/latest/2021-02-04-5b1fc7be-62f62b93/Singularity
collection: maplesond/portcullis
---

# maplesond/portcullis:latest

```bash
$ singularity pull shub://maplesond/portcullis:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: maplesond/portcullis

%labels
   Maintainer maplesond
   Version 1.2.0

%apprun portcullis
    exec portcullis

%apphelp portcullis
    Portcullis is the main tool in this container.  Use it to analyse and predict splice junctions from RNAseq alignments.  Requires a genome is fasta format and a BAM file as input.


%apprun junctools
    exec junctools

%apphelp junctools
    Junctools is a collection of miscellaneous tools for analysing, manipulating and converting junction files.
```

## Collection

 - Name: [maplesond/portcullis](https://github.com/maplesond/portcullis)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

