---
id: 3614
name: "federatedcloud/NixTemplates"
branch: "master"
tag: "nix_alpine_openmpi_5a14a0d9988b1d0dfe2a8a5c2ad2f12595d5d6c8"
commit: "0b2a95be38dee166426a2d5beb329ddafc2d154f"
version: "0c4cffb6ecc663cc0c8de6fc1b15c9c1"
build_date: "2018-07-20T15:00:37.766Z"
size_mb: 300
size: 53391391
sif: "https://datasets.datalad.org/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_5a14a0d9988b1d0dfe2a8a5c2ad2f12595d5d6c8/2018-07-20-0b2a95be-0c4cffb6/0c4cffb6ecc663cc0c8de6fc1b15c9c1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_5a14a0d9988b1d0dfe2a8a5c2ad2f12595d5d6c8/2018-07-20-0b2a95be-0c4cffb6/
recipe: https://datasets.datalad.org/shub/federatedcloud/NixTemplates/nix_alpine_openmpi_5a14a0d9988b1d0dfe2a8a5c2ad2f12595d5d6c8/2018-07-20-0b2a95be-0c4cffb6/Singularity
collection: federatedcloud/NixTemplates
---

# federatedcloud/NixTemplates:nix_alpine_openmpi_5a14a0d9988b1d0dfe2a8a5c2ad2f12595d5d6c8

```bash
$ singularity pull shub://federatedcloud/NixTemplates:nix_alpine_openmpi_5a14a0d9988b1d0dfe2a8a5c2ad2f12595d5d6c8
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: federatedcloud/NixTemplates:nix_alpine_base_14e053b44868adf9413cad2c6394cfbdfb149b81

# For development:
# Bootstrap: localimage
# From: Base/nix_alpine_base_bc4bd803c3aaa8622b493bcf66190c3944706ec3_testing.img

%environment
export TRIGGER=1
export PATH="${PATH}:/usr/local/bin"

%setup

%files
./Base/OpenMPI/config.nix /template/hometmp/.config/nixpkgs/
./Base/OpenMPI/dev-env.nix /nixenv/nixuser/
Utils/persist-env.sh /nixenv/nixuser/
./Base/OpenMPI/mpi4py_benchmarks /nixenv/nixuser/
./Base/OpenMPI/entrypoint* /nixenv/nixuser/
./Base/OpenMPI/default.nix /nixenv/nixuser/
./Base/OpenMPI/default.sh /nixenv/nixuser/

%runscript

USER=$(whoami)
echo "runscript user is $USER"

# Run the base nix runscript to initialize nix
sh /.singularity.d/runscript-nixbase

# We need to overwrite the file from base
cp -R /template/hometmp/.config/nixpkgs/* $HOME/.config/nixpkgs/

$nixenv && cd /tmp && sh /nixenv/nixuser/persist-env.sh /nixenv/nixuser/dev-env.nix

# TODO: May need this later
# cp ./Base/OpenMPI/default-mca-params.conf ${HOME}/.openmpi/mca-params.conf

#TODO: check if "$@", if not, run default.sh
# exec /bin/sh "$@"
exec /bin/sh "/nixenv/nixuser/default.sh"
```

## Collection

 - Name: [federatedcloud/NixTemplates](https://github.com/federatedcloud/NixTemplates)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

