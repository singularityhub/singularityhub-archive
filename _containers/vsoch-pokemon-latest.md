---
id: 1413
name: "vsoch/pokemon"
branch: "master"
tag: "latest"
commit: "17c7170689a2d277ebf577ed39a69225c956b22d"
version: "2e21c4838412b3c25bc73f1935f7d42f"
build_date: "2021-01-13T23:38:10.525Z"
size_mb: 673
size: 327122975
sif: "https://datasets.datalad.org/shub/vsoch/pokemon/latest/2021-01-13-17c71706-2e21c483/2e21c4838412b3c25bc73f1935f7d42f.simg"
url: https://datasets.datalad.org/shub/vsoch/pokemon/latest/2021-01-13-17c71706-2e21c483/
recipe: https://datasets.datalad.org/shub/vsoch/pokemon/latest/2021-01-13-17c71706-2e21c483/Singularity
collection: vsoch/pokemon
---

# vsoch/pokemon:latest

```bash
$ singularity pull shub://vsoch/pokemon:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

#
# sudo singularity build pokemons Singularity
#

%runscript
    if [ $# -eq 0 ]
        then
        echo "Try one of these commands:"
        exec /opt/conda/bin/scif apps
    else
        exec /opt/conda/bin/scif "$@"
    fi

%files
    pokemon.scif
    
%post
    apt-get update

    /opt/conda/bin/pip install scif
    /opt/conda/bin/pip install pokemon
    /opt/conda/bin/scif install /pokemon.scif
```

## Collection

 - Name: [vsoch/pokemon](https://github.com/vsoch/pokemon)
 - License: [MIT License](https://api.github.com/licenses/mit)

