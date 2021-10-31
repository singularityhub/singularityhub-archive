---
id: 1048
name: "ResearchIT/nwchem"
branch: "master"
tag: "6.6-openmpi"
commit: "5f290a6da42f214e60c89d10e19bcb20a178b3cb"
version: "4313f79fde2a408e727280805ad2382b"
build_date: "2017-12-07T15:25:40.550Z"
size_mb: 811
size: 259637279
sif: "https://datasets.datalad.org/shub/ResearchIT/nwchem/6.6-openmpi/2017-12-07-5f290a6d-4313f79f/4313f79fde2a408e727280805ad2382b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/nwchem/6.6-openmpi/2017-12-07-5f290a6d-4313f79f/
recipe: https://datasets.datalad.org/shub/ResearchIT/nwchem/6.6-openmpi/2017-12-07-5f290a6d-4313f79f/Singularity
collection: ResearchIT/nwchem
---

# ResearchIT/nwchem:6.6-openmpi

```bash
$ singularity pull shub://ResearchIT/nwchem:6.6-openmpi
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

# If you want the updates (available at the bootstrap date) to be installed
# inside the container during the bootstrap instead of the General Availability
# point release (7.x) then uncomment the following line
#UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/

%environment
PATH=/usr/lib64/openmpi/bin/:$PATH
export PATH

%runscript
nwchem_openmpi "$@"

%post
 yum -y install epel-release
 yum -y install nwchem nwchem-openmpi nwchem-common ga-openmpi
 echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/' >> /usr/share/nwchem/nwchem.sh
 ln -s /usr/lib64/openmpi/lib/libmpi_mpifh.so.12.0.1 /usr/lib64/openmpi/lib/libmpi_f77.so.1
 ln -s /usr/lib64/openmpi/lib/libmpi_mpifh.so.12.0.1 /usr/lib64/openmpi/lib/libmpi_f90.so.1
 ln -s /usr/lib64/openmpi/lib/libmpi.so.12.0.6 /usr/lib64/openmpi/lib/libmpi.so.1
 echo "source /usr/share/nwchem/nwchem.sh" >> /environment
 mkdir /scratch
```

## Collection

 - Name: [ResearchIT/nwchem](https://github.com/ResearchIT/nwchem)
 - License: None

