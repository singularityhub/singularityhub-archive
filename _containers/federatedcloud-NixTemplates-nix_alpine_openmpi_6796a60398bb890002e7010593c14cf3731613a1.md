---
id: 3775
name: "federatedcloud/NixTemplates"
branch: "master"
tag: "nix_alpine_openmpi_6796a60398bb890002e7010593c14cf3731613a1"
commit: "0f329fa3821e414b02c73e4703d2f55205b88b6c"
version: "1ba393dbd34b035c75fa32203bfd1a71"
build_date: "2020-11-30T21:05:39.102Z"
size_mb: 302
size: 53547039
sif: "https://datasets.datalad.org/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_6796a60398bb890002e7010593c14cf3731613a1/2020-11-30-0f329fa3-1ba393db/1ba393dbd34b035c75fa32203bfd1a71.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_6796a60398bb890002e7010593c14cf3731613a1/2020-11-30-0f329fa3-1ba393db/
recipe: https://datasets.datalad.org/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_6796a60398bb890002e7010593c14cf3731613a1/2020-11-30-0f329fa3-1ba393db/Singularity
collection: federatedcloud/NixTemplates
---

# federatedcloud/NixTemplates:nix_alpine_openmpi_6796a60398bb890002e7010593c14cf3731613a1

```bash
$ singularity pull shub://federatedcloud/NixTemplates:nix_alpine_openmpi_6796a60398bb890002e7010593c14cf3731613a1
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
sh /.singularity.d/runscript-nixbase

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

