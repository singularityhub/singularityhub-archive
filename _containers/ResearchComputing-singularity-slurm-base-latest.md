---
id: 1549
name: "ResearchComputing/singularity-slurm-base"
branch: "master"
tag: "latest"
commit: "5cbba9253a3c24bc8c98f7725dece3b332a73142"
version: "d23511ff647f9b766e24ae2e132e39bf"
build_date: "2020-11-20T10:06:38.679Z"
size_mb: 1095
size: 354254879
sif: "https://datasets.datalad.org/shub/ResearchComputing/singularity-slurm-base/latest/2020-11-20-5cbba925-d23511ff/d23511ff647f9b766e24ae2e132e39bf.simg"
url: https://datasets.datalad.org/shub/ResearchComputing/singularity-slurm-base/latest/2020-11-20-5cbba925-d23511ff/
recipe: https://datasets.datalad.org/shub/ResearchComputing/singularity-slurm-base/latest/2020-11-20-5cbba925-d23511ff/Singularity
collection: ResearchComputing/singularity-slurm-base
---

# ResearchComputing/singularity-slurm-base:latest

```bash
$ singularity pull shub://ResearchComputing/singularity-slurm-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%labels
   AUTHOR sampedro@colorado.edu

%post
   useradd -u 515 -m slurm
   useradd -u 992 -m munge
   yum -y update
   yum -y install epel-release
   yum -y groupinstall 'Development Tools'
   yum -y install sssd wget strace iproute munge munge-devel pam-devel openssl openssl-devel readline-devel perl-devel
   cd ~ && wget https://download.schedmd.com/slurm/slurm-17.02.9.tar.bz2
   rpmbuild -ta slurm-17.02.9.tar.bz2
   cd ~/rpmbuild/RPMS/x86_64
   rpm -ivh slurm-pam_slurm-17.02.9-1.el7.centos.x86_64.rpm slurm-plugins-17.02.9-1.el7.centos.x86_64.rpm slurm-munge-17.02.9-1.el7.centos.x86_64.rpm slurm-perlapi-17.02.9-1.el7.centos.x86_64.rpm slurm-17.02.9-1.el7.centos.x86_64.rpm slurm-devel-17.02.9-1.el7.centos.x86_64.rpm
```

## Collection

 - Name: [ResearchComputing/singularity-slurm-base](https://github.com/ResearchComputing/singularity-slurm-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

