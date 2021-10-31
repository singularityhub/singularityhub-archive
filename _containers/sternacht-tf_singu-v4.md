---
id: 8737
name: "sternacht/tf_singu"
branch: "master"
tag: "v4"
commit: "3984e002b02bf0f555605eb0c27209a3b3503b0a"
version: "a837d47f83b9abfad2f8e30e1bc02224"
build_date: "2019-05-01T22:22:28.604Z"
size_mb: 7278
size: 4491218975
sif: "https://datasets.datalad.org/shub/sternacht/tf_singu/v4/2019-05-01-3984e002-a837d47f/a837d47f83b9abfad2f8e30e1bc02224.simg"
url: https://datasets.datalad.org/shub/sternacht/tf_singu/v4/2019-05-01-3984e002-a837d47f/
recipe: https://datasets.datalad.org/shub/sternacht/tf_singu/v4/2019-05-01-3984e002-a837d47f/Singularity
collection: sternacht/tf_singu
---

# sternacht/tf_singu:v4

```bash
$ singularity pull shub://sternacht/tf_singu:v4
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: alan0415/singularity_tf_rdma:v8

cd /benchmarks && git checkout cnn_tf_v1.12_compatible

pip3 install absl-py
```

## Collection

 - Name: [sternacht/tf_singu](https://github.com/sternacht/tf_singu)
 - License: None

