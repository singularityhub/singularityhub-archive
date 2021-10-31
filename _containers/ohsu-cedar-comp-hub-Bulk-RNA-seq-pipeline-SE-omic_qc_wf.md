---
id: 9330
name: "ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE"
branch: "master"
tag: "omic_qc_wf"
commit: "1c6a1d8ae0b9c224deea0d9548616560b5e0e09b"
version: "314558c49dd92fdbfe2e32705b8cc588"
build_date: "2019-05-29T03:17:47.664Z"
size_mb: 3840
size: 1719283743
sif: "https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/omic_qc_wf/2019-05-29-1c6a1d8a-314558c4/314558c49dd92fdbfe2e32705b8cc588.simg"
url: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/omic_qc_wf/2019-05-29-1c6a1d8a-314558c4/
recipe: https://datasets.datalad.org/shub/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE/omic_qc_wf/2019-05-29-1c6a1d8a-314558c4/Singularity
collection: ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE
---

# ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:omic_qc_wf

```bash
$ singularity pull shub://ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE:omic_qc_wf
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    omic_qc_wf.yaml

%environment
    PATH=/opt/conda/envs/$(head -1 omic_qc_wf.yaml | cut -d' ' -f2)/bin:$PATH

%post
    apt-get update
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 omic_qc_wf.yaml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f omic_qc_wf.yaml

%runscript
    exec /bin/bash
```

## Collection

 - Name: [ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE](https://github.com/ohsu-cedar-comp-hub/Bulk-RNA-seq-pipeline-SE)
 - License: None

