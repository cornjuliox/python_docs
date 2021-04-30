import os
import pprint
import subprocess
from glob import glob

pp = pprint.PrettyPrinter(indent=2)


results: list[str] = glob(os.getcwd() + "/*/")
full_paths: list[str] = [
    x + "Dockerfile"
    for x in results
]

results: list[int] = []
for x in full_paths:
    lib_name: str = x.split("/")[-2]
    tag_name = f"local-{lib_name}-docs"
    command = [
        "docker",
        "build",
        f"-f {x}",
        f"-t {tag_name}",
        "."
    ]
    results.append(subprocess.run(command, shell=True))

print(results)
