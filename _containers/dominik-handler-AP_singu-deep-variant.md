---
id: 13131
name: "dominik-handler/AP_singu"
branch: "master"
tag: "deep-variant"
commit: "1dc31e33396133773508cd85c05710dc93ae1dc3"
version: "59c12a5fbe6c55e928458383a84f2a68aaa1f3a8b2e117149afa25d10e29dde4"
build_date: "2020-05-26T08:26:44.984Z"
size_mb: 3461.265625
size: 3629400064
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/deep-variant/2020-05-26-1dc31e33-59c12a5f/59c12a5fbe6c55e928458383a84f2a68aaa1f3a8b2e117149afa25d10e29dde4.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/deep-variant/2020-05-26-1dc31e33-59c12a5f/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/deep-variant/2020-05-26-1dc31e33-59c12a5f/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:deep-variant

```bash
$ singularity pull shub://dominik-handler/AP_singu:deep-variant
```

## Singularity Recipe

```singularity
#bedtools in singularity

Bootstrap: docker
From: google/deepvariant:latest-gpu

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  google deep variant

%runscript
    

%post


%environment

%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

