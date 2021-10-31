---
id: 1744
name: "Maaarcocr/comp3096_2018"
branch: "master"
tag: "w2v"
commit: "c6db01a43d7c6e6527c878fb4c1b2ef44137569e"
version: "210742a4966e6769a2ea90dfe4859ab1"
build_date: "2018-02-16T17:20:20.399Z"
size_mb: 719
size: 251998239
sif: "https://datasets.datalad.org/shub/Maaarcocr/comp3096_2018/w2v/2018-02-16-c6db01a4-210742a4/210742a4966e6769a2ea90dfe4859ab1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Maaarcocr/comp3096_2018/w2v/2018-02-16-c6db01a4-210742a4/
recipe: https://datasets.datalad.org/shub/Maaarcocr/comp3096_2018/w2v/2018-02-16-c6db01a4-210742a4/Singularity
collection: Maaarcocr/comp3096_2018
---

# Maaarcocr/comp3096_2018:w2v

```bash
$ singularity pull shub://Maaarcocr/comp3096_2018:w2v
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python

%setup
    mkdir ${SINGULARITY_ROOTFS}/scratch0
    mkdir ${SINGULARITY_ROOTFS}/tools

%files
    Word2vec /tools/Word2Vec
    Scripts/pass.py /tools/pass.py
    InVita/bin/InVita /tools/invita

%post 
    cd /tools/Word2Vec/dav-word2vec
    make build

%runscript
    cp -r /tools ~/
    cp /scratch0/data.txt tools/Word2Vec/dav-word2vec/bin/data.txt
    cp /scratch0/hyperParameters.json tools/hyperParameters.json
    mkdir /scratch0/output
    
    cd tools
    ls
    python pass.py "hyperParameters.json" 0 "Word2Vec/dav-word2vec/bin/word2vec"
    mv Word2Vec/dav-word2vec/bin/vec.txt /scratch0/output/
```

## Collection

 - Name: [Maaarcocr/comp3096_2018](https://github.com/Maaarcocr/comp3096_2018)
 - License: None

