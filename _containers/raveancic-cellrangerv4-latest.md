---
id: 14895
name: "raveancic/cellrangerv4"
branch: "main"
tag: "latest"
commit: "93c20ae43d03e596b07bc76c831fa4e1a1b70e5e"
version: "1dc9aee309984975e55d12d06b110df6"
build_date: "2020-11-18T13:38:36.528Z"
size_mb: 2365.0
size: 1075572767
sif: "https://datasets.datalad.org/shub/raveancic/cellrangerv4/latest/2020-11-18-93c20ae4-1dc9aee3/1dc9aee309984975e55d12d06b110df6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/raveancic/cellrangerv4/latest/2020-11-18-93c20ae4-1dc9aee3/
recipe: https://datasets.datalad.org/shub/raveancic/cellrangerv4/latest/2020-11-18-93c20ae4-1dc9aee3/Singularity
collection: raveancic/cellrangerv4
---

# raveancic/cellrangerv4:latest

```bash
$ singularity pull shub://raveancic/cellrangerv4:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic


%post
    mkdir -p /tmp/cellranger-build ¥
    && cd /tmp/cellranger-build ¥
    && apt-get update ¥
    && apt-get install -y wget ¥
    && wget -O cellranger-4.0.0.tar.gz "https://cf.10xgenomics.com/releases/cell-exp/cellranger-4.0.0.tar.gz?Expires=1605584822&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1leHAvY2VsbHJhbmdlci00LjAuMC50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2MDU1ODQ4MjJ9fX1dfQ__&Signature=dLeOXCuNyUQAgcL0YbHMzlAfTtwPjOwaHOtJIxNqIpRqn3osRQLkZqrYjtIbtl8mTn0tVRgm45uYnhivWf9RsvFm3URTjEBDH5PeSbLlanV7CCPVYJwdxopamg4Rq7GUx‾GVN2aEUOVCFpARU2PJA6jf4S42atgS3XI3LkkK7Z2fDhL88fcpOd9DyoBpE0NFxD2Mf0NrffRzL4B009dPzszUhTU9qv9tS-JfI‾so9wxhQ10gDRD9hH3uxRz‾W4HafRgzHdJjjYAZyGzL2Zwgi6z-QR5gDR1yeHsMFG1m9HAII4D06nNSfYReOrf1b9OzWCX2Dlia2nVq-TLRCxzSeQ__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA" ¥
    && mkdir /apps ¥
    && mv cellranger-4.0.0.tar.gz /apps/ ¥
    && cd /apps ¥
    && tar -xzvf cellranger-4.0.0.tar.gz ¥
    && rm -f cellranger-4.0.0.tar.gz ¥
    && rm -rf /tmp/cellranger-build

%environment
    export PATH=/apps/cellranger-4.0.0:$PATH

%labels
    Alessandro Raveane
    Version v0.0.1
```

## Collection

 - Name: [raveancic/cellrangerv4](https://github.com/raveancic/cellrangerv4)
 - License: None

