---
id: 14244
name: "CallumWalley/RSE20_tidyverse_long"
branch: "master"
tag: "latest"
commit: "2fa94d55f68e031f72f6734a8544ac7eb3b3294d"
version: "0bef3ed3eaf11150b88c71277fc629e9"
build_date: "2020-11-24T18:19:46.095Z"
size_mb: 2023.0
size: 716079135
sif: "https://datasets.datalad.org/shub/CallumWalley/RSE20_tidyverse_long/latest/2020-11-24-2fa94d55-0bef3ed3/0bef3ed3eaf11150b88c71277fc629e9.sif"
url: https://datasets.datalad.org/shub/CallumWalley/RSE20_tidyverse_long/latest/2020-11-24-2fa94d55-0bef3ed3/
recipe: https://datasets.datalad.org/shub/CallumWalley/RSE20_tidyverse_long/latest/2020-11-24-2fa94d55-0bef3ed3/Singularity
collection: CallumWalley/RSE20_tidyverse_long
---

# CallumWalley/RSE20_tidyverse_long:latest

```bash
$ singularity pull shub://CallumWalley/RSE20_tidyverse_long:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/tidyverse:3.6.1

%labels
  Author Pawsey Supercomputing Centre
  Version 0.0.1

%startscript
  export R_PORT=${R_PORT:-"8787"}
  export R_ADDRESS=${R_ADDRESS:-"0.0.0.0"}
  
  rserver --www-port $R_PORT --www-address $R_ADDRESS --auth-none=1 --auth-validate-users=0
```

## Collection

 - Name: [CallumWalley/RSE20_tidyverse_long](https://github.com/CallumWalley/RSE20_tidyverse_long)
 - License: None

