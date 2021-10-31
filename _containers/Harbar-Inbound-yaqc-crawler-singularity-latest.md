---
id: 9740
name: "Harbar-Inbound/yaqc-crawler-singularity"
branch: "master"
tag: "latest"
commit: "33f738f536a4d1019aeb815f7d46503dda35eb75"
version: "1fb3b1766201f64d3179058b0da171f6"
build_date: "2019-06-25T18:43:29.663Z"
size_mb: 142
size: 48267295
sif: "https://datasets.datalad.org/shub/Harbar-Inbound/yaqc-crawler-singularity/latest/2019-06-25-33f738f5-1fb3b176/1fb3b1766201f64d3179058b0da171f6.simg"
url: https://datasets.datalad.org/shub/Harbar-Inbound/yaqc-crawler-singularity/latest/2019-06-25-33f738f5-1fb3b176/
recipe: https://datasets.datalad.org/shub/Harbar-Inbound/yaqc-crawler-singularity/latest/2019-06-25-33f738f5-1fb3b176/Singularity
collection: Harbar-Inbound/yaqc-crawler-singularity
---

# Harbar-Inbound/yaqc-crawler-singularity:latest

```bash
$ singularity pull shub://Harbar-Inbound/yaqc-crawler-singularity:latest
```

## Singularity Recipe

```singularity
#
#     Copyright 2019 Jeroen Galjaard
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

Bootstrap: docker
From: yaqc/crawler:slurm

%apprun crawler
exec python3 /app/crawler.py
```

## Collection

 - Name: [Harbar-Inbound/yaqc-crawler-singularity](https://github.com/Harbar-Inbound/yaqc-crawler-singularity)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

