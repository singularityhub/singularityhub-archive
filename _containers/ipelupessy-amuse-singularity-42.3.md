---
id: 2573
name: "ipelupessy/amuse-singularity"
branch: "master"
tag: "42.3"
commit: "083128d77c603018093bfa17adddfa05bf132b49"
version: "60f2187e0535fba2103554e53766ef2e"
build_date: "2018-04-20T05:38:16.608Z"
size_mb: 450
size: 184012831
sif: "https://datasets.datalad.org/shub/ipelupessy/amuse-singularity/42.3/2018-04-20-083128d7-60f2187e/60f2187e0535fba2103554e53766ef2e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ipelupessy/amuse-singularity/42.3/2018-04-20-083128d7-60f2187e/
recipe: https://datasets.datalad.org/shub/ipelupessy/amuse-singularity/42.3/2018-04-20-083128d7-60f2187e/Singularity
collection: ipelupessy/amuse-singularity
---

# ipelupessy/amuse-singularity:42.3

```bash
$ singularity pull shub://ipelupessy/amuse-singularity:42.3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: opensuse:42.3

%runscript
    python "$@"

%post
    zypper -n install libpsm_infinipath1
    zypper ar https://download.opensuse.org/repositories/home:/pelupes:/amuse/openSUSE_Leap_42.3/ amuse
    zypper --gpg-auto-import-keys refresh amuse
    echo "install amuse..."
    zypper -n install amuse
```

## Collection

 - Name: [ipelupessy/amuse-singularity](https://github.com/ipelupessy/amuse-singularity)
 - License: None

