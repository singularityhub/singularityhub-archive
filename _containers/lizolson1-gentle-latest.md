---
id: 12306
name: "lizolson1/gentle"
branch: "master"
tag: "latest"
commit: "6bf40189a750291f4a293a7a668c09b15e04d212"
version: "75210e7887a3f4c5cb42cfb0f879611d"
build_date: "2020-02-19T05:22:51.664Z"
size_mb: 1190.0
size: 618627103
sif: "https://datasets.datalad.org/shub/lizolson1/gentle/latest/2020-02-19-6bf40189-75210e78/75210e7887a3f4c5cb42cfb0f879611d.sif"
url: https://datasets.datalad.org/shub/lizolson1/gentle/latest/2020-02-19-6bf40189-75210e78/
recipe: https://datasets.datalad.org/shub/lizolson1/gentle/latest/2020-02-19-6bf40189-75210e78/Singularity
collection: lizolson1/gentle
---

# lizolson1/gentle:latest

```bash
$ singularity pull shub://lizolson1/gentle:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: lowerquality/gentle:latest


%post
	#test
	apt-get -y update
 	apt-get -y install vim
```

## Collection

 - Name: [lizolson1/gentle](https://github.com/lizolson1/gentle)
 - License: None

