---
id: 11726
name: "jacobhepkema/scanem-wip"
branch: "master"
tag: "latest"
commit: "2b94d2adf01458c3dc171c23bb174dc7f100d9a2"
version: "725340d483998e074690ef390d12a5fe"
build_date: "2020-01-08T11:56:07.904Z"
size_mb: 735.0
size: 272003103
sif: "https://datasets.datalad.org/shub/jacobhepkema/scanem-wip/latest/2020-01-08-2b94d2ad-725340d4/725340d483998e074690ef390d12a5fe.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jacobhepkema/scanem-wip/latest/2020-01-08-2b94d2ad-725340d4/
recipe: https://datasets.datalad.org/shub/jacobhepkema/scanem-wip/latest/2020-01-08-2b94d2ad-725340d4/Singularity
collection: jacobhepkema/scanem-wip
---

# jacobhepkema/scanem-wip:latest

```bash
$ singularity pull shub://jacobhepkema/scanem-wip:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: julia:1.2.0

%help
    Julia 1.2

%labels
    Maintainer @jacobhepkema
    Version v0.9

%post
    JULIA_PKGDIR=/opt/julia
    JULIA_VERSION=1.2.0
    export JULIA_DEPOT_PATH=/opt/julia
    export JULIA_PATH=/usr/local/julia
    export PATH=$JULIA_PATH/bin:$PATH

    mkdir -p "$JULIA_DEPOT_PATH"
    
    # Will this make 'ps' work?
    apt-get update && apt-get install -y procps

    julia -e 'using Pkg;pkg"add Dates Parsers PooledArrays WeakRefStrings FilePathsBase LazyArrays Libdl Mmap CategoricalArrays Missings InvertedIndices Tables TableTraits IteratorInterfaceExtensions DataAPI Unicode SortingAlgorithms Reexport TextWrap Compat Blosc ArgParse DataFrames CSV Profile Random Statistics HDF5;precompile"'

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

 - Name: [jacobhepkema/scanem-wip](https://github.com/jacobhepkema/scanem-wip)
 - License: None

