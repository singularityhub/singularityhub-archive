---
id: 8270
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs8_py36"
commit: "f614029c90ba943ba59fd5df686375b370460c47"
version: "e6bbf7a04319a1b4cf33dbba033a9918"
build_date: "2019-04-08T08:50:10.983Z"
size_mb: 1079
size: 373698591
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36/2019-04-08-f614029c-e6bbf7a0/e6bbf7a04319a1b4cf33dbba033a9918.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36/2019-04-08-f614029c-e6bbf7a0/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36/2019-04-08-f614029c-e6bbf7a0/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs8_py36

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs8_py36
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:devtoolset8

%post
   # install python36
   yum install -y https://centos7.iuscommunity.org/ius-release.rpm
   yum update -y
   yum install -y python36u python36u-libs python36u-devel python36u-pip
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

