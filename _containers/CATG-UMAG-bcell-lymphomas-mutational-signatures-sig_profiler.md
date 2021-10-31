---
id: 15894
name: "CATG-UMAG/bcell-lymphomas-mutational-signatures"
branch: "main"
tag: "sig_profiler"
commit: "1fa0593212c7a93e3afd31f9f5163fd334c47380"
version: "b3b880cb63ae608dab69a0a3508a2b719a74778418327cede6b437785d24a7be"
build_date: "2021-04-13T06:17:39.208Z"
size_mb: 1626.28515625
size: 1705283584
sif: "https://datasets.datalad.org/shub/CATG-UMAG/bcell-lymphomas-mutational-signatures/sig_profiler/2021-04-13-1fa05932-b3b880cb/b3b880cb63ae608dab69a0a3508a2b719a74778418327cede6b437785d24a7be.sif"
url: https://datasets.datalad.org/shub/CATG-UMAG/bcell-lymphomas-mutational-signatures/sig_profiler/2021-04-13-1fa05932-b3b880cb/
recipe: https://datasets.datalad.org/shub/CATG-UMAG/bcell-lymphomas-mutational-signatures/sig_profiler/2021-04-13-1fa05932-b3b880cb/Singularity
collection: CATG-UMAG/bcell-lymphomas-mutational-signatures
---

# CATG-UMAG/bcell-lymphomas-mutational-signatures:sig_profiler

```bash
$ singularity pull shub://CATG-UMAG/bcell-lymphomas-mutational-signatures:sig_profiler
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:1.5.1-cuda10.1-cudnn7-runtime


%labels
    Author Diego Alvarez (dialvarezs@gmail.com)
    Description Contains SigProfilerExtractor (v1.1.0) and its dependencies

%post
    apt update && apt upgrade -y
    /opt/conda/bin/conda install -y "numpy>=1.18.5"
    /opt/conda/bin/pip install --no-cache-dir SigProfilerExtractor==1.1.0

%test
    /opt/conda/bin/python3 -c "import SigProfilerExtractor"
```

## Collection

 - Name: [CATG-UMAG/bcell-lymphomas-mutational-signatures](https://github.com/CATG-UMAG/bcell-lymphomas-mutational-signatures)
 - License: [MIT License](https://api.github.com/licenses/mit)

