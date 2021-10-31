---
id: 6132
name: "gearslaboratory/gears-singularity"
branch: "master"
tag: "gears-cloudcompare"
commit: "5e52e260c8f22ded9575f7f415b319feaf777b07"
version: "7d7f50c7989e3b2b696791bd2c68f306"
build_date: "2019-04-18T09:01:49.420Z"
size_mb: 2886
size: 1033457695
sif: "https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-cloudcompare/2019-04-18-5e52e260-7d7f50c7/7d7f50c7989e3b2b696791bd2c68f306.simg"
url: https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-cloudcompare/2019-04-18-5e52e260-7d7f50c7/
recipe: https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-cloudcompare/2019-04-18-5e52e260-7d7f50c7/Singularity
collection: gearslaboratory/gears-singularity
---

# gearslaboratory/gears-singularity:gears-cloudcompare

```bash
$ singularity pull shub://gearslaboratory/gears-singularity:gears-cloudcompare
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tswetnam/cloudcompare:latest

%post
  apt-get clean
  apt-get -y update
  apt-get -y install xvfb  

%runscript
	Xvfb :0 -screen 0 1024x768x16 &
```

## Collection

 - Name: [gearslaboratory/gears-singularity](https://github.com/gearslaboratory/gears-singularity)
 - License: None

