---
id: 12246
name: "jacobhepkema/singularity-bio-julia"
branch: "master"
tag: "latest"
commit: "b059107e72569e03181ffef82848c664f984576c"
version: "224fe936020ac5b19e47764f2cbb7073"
build_date: "2020-02-10T13:23:04.347Z"
size_mb: 789.0
size: 289447967
sif: "https://datasets.datalad.org/shub/jacobhepkema/singularity-bio-julia/latest/2020-02-10-b059107e-224fe936/224fe936020ac5b19e47764f2cbb7073.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jacobhepkema/singularity-bio-julia/latest/2020-02-10-b059107e-224fe936/
recipe: https://datasets.datalad.org/shub/jacobhepkema/singularity-bio-julia/latest/2020-02-10-b059107e-224fe936/Singularity
collection: jacobhepkema/singularity-bio-julia
---

# jacobhepkema/singularity-bio-julia:latest

```bash
$ singularity pull shub://jacobhepkema/singularity-bio-julia:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: julia:1.2.0

%help
    Julia 1.2

%labels
    Maintainer @jacobhepkema
    Version v0.1

%post
    JULIA_PKGDIR=/opt/julia
    JULIA_VERSION=1.2.0
    export JULIA_DEPOT_PATH=/opt/julia
    export JULIA_PATH=/usr/local/julia
    export PATH=$JULIA_PATH/bin:$PATH

    mkdir -p "$JULIA_DEPOT_PATH"
    
    # Will this make 'ps' work?
    apt-get update && apt-get install -y procps

    julia -e 'using Pkg;pkg"add Dates Parsers PooledArrays WeakRefStrings FilePathsBase LazyArrays Libdl Mmap CategoricalArrays Missings InvertedIndices Tables TableTraits IteratorInterfaceExtensions DataAPI Unicode SortingAlgorithms Reexport TextWrap Compat Blosc ArgParse DataFrames CSV Profile Random Statistics HDF5 BioSequences Bio DelimitedFiles;precompile"'

    chmod -R 777 /opt
    chmod -R 777 /usr/local/julia

%environment
    export JULIA_DEPOT_PATH=/opt/julia
    export JULIA_PKGDIR=/opt/julia
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export JULIA_PATH=/usr/local/julia
    export PATH=$JULIA_PATH/bin:$PATH

# smoke test
julia --version

%runscript
    exec julia -e "$@"
```

## Collection

 - Name: [jacobhepkema/singularity-bio-julia](https://github.com/jacobhepkema/singularity-bio-julia)
 - License: None

