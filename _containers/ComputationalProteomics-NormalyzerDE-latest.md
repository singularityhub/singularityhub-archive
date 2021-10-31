---
id: 15137
name: "ComputationalProteomics/NormalyzerDE"
branch: "singularity"
tag: "latest"
commit: "25363aa372d62c6b1a5530c53a3632072bf39723"
version: "5847a2a952107483a9e2daf6cf2692be"
build_date: "2021-02-02T07:46:46.605Z"
size_mb: 4340.0
size: 1459728415
sif: "https://datasets.datalad.org/shub/ComputationalProteomics/NormalyzerDE/latest/2021-02-02-25363aa3-5847a2a9/5847a2a952107483a9e2daf6cf2692be.sif"
url: https://datasets.datalad.org/shub/ComputationalProteomics/NormalyzerDE/latest/2021-02-02-25363aa3-5847a2a9/
recipe: https://datasets.datalad.org/shub/ComputationalProteomics/NormalyzerDE/latest/2021-02-02-25363aa3-5847a2a9/Singularity
collection: ComputationalProteomics/NormalyzerDE
---

# ComputationalProteomics/NormalyzerDE:latest

```bash
$ singularity pull shub://ComputationalProteomics/NormalyzerDE:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: bioconductor/bioconductor_docker

# Last build date: 202117
# Test build locally with singularity build test_out.simg Singularity

%post

    Rscript -e 'install.packages("devtools")'
    Rscript -e 'devtools::install_github("ComputationalProteomics/NormalyzerDE", dependencies=TRUE)'
```

## Collection

 - Name: [ComputationalProteomics/NormalyzerDE](https://github.com/ComputationalProteomics/NormalyzerDE)
 - License: None

