#!/usr/bin/env python3

import json
import requests
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
images = os.path.join(root, "_data", "images.json")
images_dir = os.path.join(root, "_images")

with open(images, "r") as fd:
    images = json.loads(fd.read())

collection_template = """---
id: %s
full_name: "%s"
images: %s
---
"""

template = """---
id: %s
name: "%s"
branch: "%s"
tag: "%s"
commit: "%s"
version: "%s"
build_date: "%s"
size_mb: %s
size: %s
sif: "%s"
datalad_url: %s
recipe: %s
collection: %s
---

# %s

```bash
$ singularity pull shub://%s
```

## Singularity Recipe

```singularity
%s
```

## Collection

 - Name: [%s](https://github.com/%s)
 - License: %s

"""

# Create collection entries first
count = 0
for cid, meta in images["collections"].items():

    filename = "%s.md" % meta["full_name"].replace("/", "-")
    filename = os.path.join(root, "_collection", filename)
    if os.path.exists(filename):
        continue

    print(
        "Parsing collection %s: %s of %s"
        % (meta["full_name"], count, len(images["collections"]))
    )

    image_ids = []
    for reponame, imageset in images["images"].items():
        for image in imageset:
            if str(image["collection"]) == str(cid):
                image_ids.append(
                    "%s-%s"
                    % (reponame.replace("/", "-"), image["tag"].replace("/", "-"))
                )

    # Don't bother rendering empty collections
    if not image_ids:
        continue

    image_ids = "\n" + "\n".join(['  - "%s"' % im for im in image_ids])
    content = collection_template % (cid, meta["full_name"], image_ids)

    with open(filename, "w") as fd:
        fd.write(content)
        count += 1


count = 0
for reponame, imageset in images["images"].items():

    print("Parsing images %s: %s of %s" % (reponame, count, len(images["images"])))

    for image in imageset:
        m = image
        filename = "%s-%s.md" % (reponame.replace("/", "-"), m["tag"].replace("/", "-"))
        filename = os.path.join(root, "_containers", filename)
        if os.path.exists(filename):
            continue

        # Generate path to datalad Singularity recipe
        dirname = os.path.dirname(image["file"])
        url = "https://datasets.datalad.org/shub/%s/Singularity" % dirname
        content = requests.get(url)
        collection = images["collections"][str(image["collection"])]
        license = "None"
        if collection.get("license"):
            license = collection.get("license")
            license = "[%s](%s)" % (license["name"], license["url"])
        sif = "https://datasets.datalad.org/shub/%s" % (m["file"])
        baseurl = "https://datasets.datalad.org?dir=/shub/%s/" % dirname
        container_name = "%s:%s" % (reponame, m["tag"])
        recipe = template % (
            m["id"],
            reponame,
            m["branch"],
            m["tag"],
            m["commit"],
            m["version"],
            m["build_date"],
            m["size_mb"],
            m["size"],
            sif,
            baseurl,
            url,
            collection["full_name"],
            container_name,
            container_name,
            content.text.strip(),
            reponame,
            reponame,
            license,
        )
        with open(filename, "w") as fd:
            fd.write(recipe)
    count += 1
