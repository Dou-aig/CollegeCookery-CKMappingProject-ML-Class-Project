
import os
 
FOLDER = "cmssprojphotos"   # name of your photos folder
EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".webp")
 
files = sorted(f for f in os.listdir(FOLDER) if f.lower().endswith(EXTENSIONS))
 
with open("images.js", "w") as out:
    out.write("const PHOTOS = [\n")
    for f in files:
        out.write('  "%s/%s",\n' % (FOLDER, f))
    out.write("];\n")
 
print("Wrote images.js with %d photos." % len(files))
 