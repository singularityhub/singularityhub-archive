---
id: 15015
name: "jolars/hessian-screening-code"
branch: "main"
tag: "latest"
commit: "33e9476829eaf5d17fe2f73dbe959d915af4964a"
version: "e32bafcd31457bc66a504f4655e5c0d6e14f9beba0e5541ddc28fc909dd083dc"
build_date: "2020-12-16T12:56:00.694Z"
size_mb: 1082.59765625
size: 1135185920
sif: "https://datasets.datalad.org/shub/jolars/hessian-screening-code/latest/2020-12-16-33e94768-e32bafcd/e32bafcd31457bc66a504f4655e5c0d6e14f9beba0e5541ddc28fc909dd083dc.sif"
url: https://datasets.datalad.org/shub/jolars/hessian-screening-code/latest/2020-12-16-33e94768-e32bafcd/
recipe: https://datasets.datalad.org/shub/jolars/hessian-screening-code/latest/2020-12-16-33e94768-e32bafcd/Singularity
collection: jolars/hessian-screening-code
---

# jolars/hessian-screening-code:latest

```bash
$ singularity pull shub://jolars/hessian-screening-code:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
from: julia:1.5.3-buster

%files
    src /Project/src
    scripts /Project/scripts
    Manifest.toml /Project
    Project.toml /Project

%environment
    export JULIA_DEPOT_PATH=:/user/.julia
    export PATH=/usr/local/julia/bin:$PATH

%post
    export JULIA_DEPOT_PATH=/user/.julia
    export PATH=/usr/local/julia/bin:$PATH

    cd Project

    julia --project -e 'using Pkg; Pkg.rm.(Any[])'
    julia --project -e 'using Pkg; Pkg.instantiate()'
    julia --project -e 'using Pkg; Pkg.precompile()'

    chmod -R a+rX $JULIA_DEPOT_PATH
    chmod -R a+rX /Project/scripts

%runscript
    if [ -z "$@" ]; then
        # if theres none, test julia:
        julia --project=/Project -e 'using Pkg;  Pkg.status()'
    else
        # if theres an argument, then run it! and hope its a julia script :)
        julia --project=/Project -e "include(\"/Project/scripts/simulations/$@\")"
    fi
```

## Collection

 - Name: [jolars/hessian-screening-code](https://github.com/jolars/hessian-screening-code)
 - License: None

