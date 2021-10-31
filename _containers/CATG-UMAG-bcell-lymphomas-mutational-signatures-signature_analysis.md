---
id: 15900
name: "CATG-UMAG/bcell-lymphomas-mutational-signatures"
branch: "main"
tag: "signature_analysis"
commit: "8c1fc415e5bbd8c19338c6ca063101857951eb3a"
version: "9e621b7280e4e2a327612d544bf4dc3c2206fe0de5ed5ed7be9d4e43e1d14c67"
build_date: "2021-04-15T02:56:55.556Z"
size_mb: 1335.0703125
size: 1399922688
sif: "https://datasets.datalad.org/shub/CATG-UMAG/bcell-lymphomas-mutational-signatures/signature_analysis/2021-04-15-8c1fc415-9e621b72/9e621b7280e4e2a327612d544bf4dc3c2206fe0de5ed5ed7be9d4e43e1d14c67.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/CATG-UMAG/bcell-lymphomas-mutational-signatures/signature_analysis/2021-04-15-8c1fc415-9e621b72/
recipe: https://datasets.datalad.org/shub/CATG-UMAG/bcell-lymphomas-mutational-signatures/signature_analysis/2021-04-15-8c1fc415-9e621b72/Singularity
collection: CATG-UMAG/bcell-lymphomas-mutational-signatures
---

# CATG-UMAG/bcell-lymphomas-mutational-signatures:signature_analysis

```bash
$ singularity pull shub://CATG-UMAG/bcell-lymphomas-mutational-signatures:signature_analysis
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: r-base:4.0.5


%labels
    Author Diego Alvarez (dialvarezs@gmail.com)
    Description Contains Jupyter with IRkernel an some R packages (nnls,tidyverse,deconstructSigs mainly)

%post
    apt update -y && apt upgrade -y
    # install packages. use precompiled R packages to reduce container creation time
    apt install -y procps python3-pip \
        r-cran-cluster r-cran-cowplot r-cran-r.utils r-cran-factoextra r-cran-irkernel r-cran-nnls r-cran-tidyverse \
        r-cran-biocmanager r-bioc-bsgenome r-bioc-genomeinfodb r-bioc-variantannotation

    # install jupyter
    pip3 install jupyter jupyterlab nbconvert

    # install deconstructSigs
    R -e "BiocManager::install('deconstructSigs')"
    # install R jupyter kernel
    R -e "IRkernel::installspec()"
```

## Collection

 - Name: [CATG-UMAG/bcell-lymphomas-mutational-signatures](https://github.com/CATG-UMAG/bcell-lymphomas-mutational-signatures)
 - License: [MIT License](https://api.github.com/licenses/mit)

