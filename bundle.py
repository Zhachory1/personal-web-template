from pathlib import Path
import shutil
import subprocess

SOURCE = Path("src")
OUTPUT = Path("public")

if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
shutil.copytree(SOURCE, OUTPUT, ignore=shutil.ignore_patterns(".gitignore"))

for source in OUTPUT.rglob("*.js"):
    destination = source.with_name(f"{source.stem}.min.js")
    result = subprocess.run(
        ["uglifyjs", "--mangle", "--compress", "--toplevel"],
        input=source.read_bytes(),
        capture_output=True,
        check=True,
    )
    destination.write_bytes(result.stdout)
    source.unlink()
