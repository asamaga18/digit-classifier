# convert_tfjs.py
import os, shutil, numpy as np

# Patch older tensorflowjs with newer NumPy
if not hasattr(np, "object"): np.object = object
if not hasattr(np, "bool"):   np.bool   = bool

from tensorflowjs.converters import converter

# Work in a path WITHOUT SPACES to avoid converter's naive split
workdir = os.path.abspath("work")
os.makedirs(workdir, exist_ok=True)

src_model = os.path.abspath("model.keras")
dst_model = os.path.join(workdir, "model.keras")
if os.path.exists(src_model) and not os.path.samefile(src_model, dst_model):
    shutil.copy2(src_model, dst_model)

os.chdir(workdir)
# IMPORTANT: converter.main expects a SINGLE STRING element and then does .split(' ')
# Since our filenames have NO spaces here, this is safe.
arg_str = "--input_format=keras model.keras web-model"
converter.main([arg_str])

print("✅ Done. Check:", os.path.join(workdir, "web-model"))

