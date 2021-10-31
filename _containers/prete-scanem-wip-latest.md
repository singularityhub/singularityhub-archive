---
id: 11718
name: "prete/scanem-wip"
branch: "master"
tag: "latest"
commit: "fce53e36319d8cdc9383e93b1365ea2f6a4abf8e"
version: "f9282dbf4168ff86959b2c523c9858f2"
build_date: "2019-11-27T11:17:56.087Z"
size_mb: 711.0
size: 254005279
sif: "https://datasets.datalad.org/shub/prete/scanem-wip/latest/2019-11-27-fce53e36-f9282dbf/f9282dbf4168ff86959b2c523c9858f2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/prete/scanem-wip/latest/2019-11-27-fce53e36-f9282dbf/
recipe: https://datasets.datalad.org/shub/prete/scanem-wip/latest/2019-11-27-fce53e36-f9282dbf/Singularity
collection: prete/scanem-wip
---

# prete/scanem-wip:latest

```bash
$ singularity pull shub://prete/scanem-wip:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: julia:1.2.0


%help
    Julia 1.2 docker image


%post
    JULIA_PKGDIR=/opt/julia
    JULIA_VERSION=1.2.0
    export JULIA_DEPOT_PATH=/opt/julia
    export JULIA_PATH=/usr/local/julia
    export PATH=$JULIA_PATH/bin:$PATH

    mkdir -p "$JULIA_DEPOT_PATH"

    julia -e 'using Pkg;pkg"add Dates Parsers PooledArrays WeakRefStrings FilePathsBase LazyArrays Libdl Mmap CategoricalArrays Missings InvertedIndices Tables TableTraits IteratorInterfaceExtensions DataAPI Unicode SortingAlgorithms Reexport TextWrap Compat Blosc ArgParse DataFrames CSV Profile Random Statistics HDF5;precompile"'

#    COMPILEFOLDER=/opt/julia/compiled/v1.2/
#
#    mkdir -p "$COMPILEFOLDER/ArgParse" && \
#    mkdir -p "$COMPILEFOLDER/HDF5" && \
#    mkdir -p "$COMPILEFOLDER/Profile" && \
#    mkdir -p "$COMPILEFOLDER/DataFrames" && \
#    mkdir -p "$COMPILEFOLDER/CSV" && \
#    mkdir -p "$COMPILEFOLDER/Statistics"
#
#    julia -e "Base.compilecache(Base.PkgId(\"ArgParse\"))" && \
#    julia -e "Base.compilecache(Base.PkgId(\"HDF5\"))" && \
#    julia -e "Base.compilecache(Base.PkgId(\"Profile\"))" && \
#    julia -e "Base.compilecache(Base.PkgId(\"DataFrames\"))" && \
#    julia -e "Base.compilecache(Base.PkgId(\"CSV\"))" && \
#    julia -e "Base.compilecache(Base.PkgId(\"Statistics\"))"

    chmod -R 777 /opt
    chmod -R 777 /usr/local/julia

%environment
    export JULIA_DEPOT_PATH=/opt/julia
    export JULIA_PKGDIR=/opt/julia
#    export COMPILEFOLDER=/opt/julia/compiled/v1.2/
#    export JULIA_LOAD_PATH=$COMPILEFOLDER:/usr/local/julia/share/julia/stdlib/v1.2
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8

julia --version


%runscript
    exec julia -e "$@"
```

## Collection

 - Name: [prete/scanem-wip](https://github.com/prete/scanem-wip)
 - License: None

