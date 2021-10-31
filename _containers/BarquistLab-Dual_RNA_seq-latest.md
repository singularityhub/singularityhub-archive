---
id: 10801
name: "BarquistLab/Dual_RNA_seq"
branch: "master"
tag: "latest"
commit: "bf233a158699702a8828f90394d09dae016f1fd0"
version: "e93e5d477a0c26f04b962da0a28f108c"
build_date: "2020-03-03T10:40:13.764Z"
size_mb: 1536.0
size: 504369183
sif: "https://datasets.datalad.org/shub/BarquistLab/Dual_RNA_seq/latest/2020-03-03-bf233a15-e93e5d47/e93e5d477a0c26f04b962da0a28f108c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/BarquistLab/Dual_RNA_seq/latest/2020-03-03-bf233a15-e93e5d47/
recipe: https://datasets.datalad.org/shub/BarquistLab/Dual_RNA_seq/latest/2020-03-03-bf233a15-e93e5d47/Singularity
collection: BarquistLab/Dual_RNA_seq
---

# BarquistLab/Dual_RNA_seq:latest

```bash
$ singularity pull shub://BarquistLab/Dual_RNA_seq:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nfcore/base


%environment

    PATH=/opt/conda/envs/BarquistLab-Dual_RNA_seq/bin:$PATH
    export PATH


%files
    environment.yml 

%post

    alias conda="/opt/conda/bin/conda"    

    /opt/conda/bin/conda env create -f /environment.yml
    conda clean --tarballs --index-cache --source-cache
```

## Collection

 - Name: [BarquistLab/Dual_RNA_seq](https://github.com/BarquistLab/Dual_RNA_seq)
 - License: None

