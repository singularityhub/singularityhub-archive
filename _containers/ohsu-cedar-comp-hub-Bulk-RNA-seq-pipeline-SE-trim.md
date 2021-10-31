---
id: 9736
name: "ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE"
branch: "master"
tag: "trim"
commit: "183376fa390e131e55749a0562fa7773323ed35f"
version: "4d3bffa11564c5007f6b0307f064d18c"
build_date: "2019-06-10T23:33:39.528Z"
size_mb: 1371
size: 723021855
sif: "https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/trim/2019-06-10-183376fa-4d3bffa1/4d3bffa11564c5007f6b0307f064d18c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/trim/2019-06-10-183376fa-4d3bffa1/
recipe: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/trim/2019-06-10-183376fa-4d3bffa1/Singularity
collection: ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE
---

# ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:trim

```bash
$ singularity pull shub://ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:trim
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: docker://continuumio/miniconda3:4.4.10

%files
    trim.yaml

%environment
    PATH="/opt/conda/envs/$(head -1 trim.yaml | cut -d' ' -f2)/bin:$PATH"

%post
    export PATH="/opt/conda/bin:$PATH"
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 trim.yaml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f trim.yaml

%runscript
    exec /bin/bash
```

## Collection

 - Name: [ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE](https://github.com/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE)
 - License: None

