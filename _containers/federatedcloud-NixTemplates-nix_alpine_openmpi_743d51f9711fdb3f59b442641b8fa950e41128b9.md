---
id: 5668
name: "federatedcloud/NixTemplates"
branch: "master"
tag: "nix_alpine_openmpi_743d51f9711fdb3f59b442641b8fa950e41128b9"
commit: "8ad0d6984f7f954e650e1b5baab3a2113ba7926d"
version: "f35399d960a1640a8e695e659193a847"
build_date: "2018-11-21T17:32:10.167Z"
size_mb: 302
size: 53547039
sif: "https://datasets.datalad.org/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_743d51f9711fdb3f59b442641b8fa950e41128b9/2018-11-21-8ad0d698-f35399d9/f35399d960a1640a8e695e659193a847.simg"
url: https://datasets.datalad.org/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_743d51f9711fdb3f59b442641b8fa950e41128b9/2018-11-21-8ad0d698-f35399d9/
recipe: https://datasets.datalad.org/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_743d51f9711fdb3f59b442641b8fa950e41128b9/2018-11-21-8ad0d698-f35399d9/Singularity
collection: federatedcloud/NixTemplates
---

# federatedcloud/NixTemplates:nix_alpine_openmpi_743d51f9711fdb3f59b442641b8fa950e41128b9

```bash
$ singularity pull shub://federatedcloud/NixTemplates:nix_alpine_openmpi_743d51f9711fdb3f59b442641b8fa950e41128b9
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: federatedcloud/NixTemplates:nix_alpine_base_e51467b4ad06617b8b104f6c9066df915fb4dfbd

# For development:
# Bootstrap: localimage
# From: Base/nix_alpine_base_bc4bd803c3aaa8622b493bcf66190c3944706ec3_testing.img

%environment
export TRIGGER=1
export PATH="${PATH}:/usr/local/bin"

%setup

%files
Utils/persist-env.sh /nixenv/nixuser/
OpenMPI/config.nix /template/hometmp/.config/nixpkgs/
OpenMPI/dev-env.nix /nixenv/nixuser/
OpenMPI/mpi4py_benchmarks /nixenv/nixuser/
OpenMPI/entrypoint* /nixenv/nixuser/
OpenMPI/default.nix /nixenv/nixuser/
OpenMPI/default.sh /nixenv/nixuser/

%runscript

# Run the base nix runscript to initialize nix
source /.singularity.d/runscript-nixbase

# We need to overwrite the file from base
cp -R /template/hometmp/.config/nixpkgs/* $HOME/.config/nixpkgs/

$nixenv && cd /tmp && sh /nixenv/nixuser/persist-env.sh /nixenv/nixuser/dev-env.nix

# TODO: May need this later
# cp default-mca-params.conf ${HOME}/.openmpi/mca-params.conf

#TODO: check if "$@", if not, run default.sh
# exec /bin/sh "$@"
exec /bin/sh "/nixenv/nixuser/default.sh"
```

## Collection

 - Name: [federatedcloud/NixTemplates](https://github.com/federatedcloud/NixTemplates)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

