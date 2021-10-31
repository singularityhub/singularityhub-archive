---
id: 9326
name: "ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE"
branch: "master"
tag: "deseq2_qc"
commit: "6cf58e9d84080805a3beaf08bca0e547abe6152c"
version: "3675aeb8d40ccc3921f0089f8b7c3b1e"
build_date: "2019-05-28T19:47:11.574Z"
size_mb: 2164
size: 970600479
sif: "https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/deseq2_qc/2019-05-28-6cf58e9d-3675aeb8/3675aeb8d40ccc3921f0089f8b7c3b1e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/deseq2_qc/2019-05-28-6cf58e9d-3675aeb8/
recipe: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/deseq2_qc/2019-05-28-6cf58e9d-3675aeb8/Singularity
collection: ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE
---

# ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:deseq2_qc

```bash
$ singularity pull shub://ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:deseq2_qc
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    deseq2_QC.yaml

%environment
    PATH=/opt/conda/envs/$(head -1 deseq2_QC.yaml | cut -d' ' -f2)/bin:$PATH

%post
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 deseq2_QC.yaml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f deseq2_QC.yaml

%runscript
    exec /bin/bash
```

## Collection

 - Name: [ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE](https://github.com/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE)
 - License: None

