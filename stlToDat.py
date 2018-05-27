#!/usr/bin/python
"""
Convert a STL to a LDRAW compatible DAT file.
It is assumed that the STL file units are millimeters.

Hazen 12/15
"""

import os
import sys

if (len(sys.argv) < 2):
    print("usage: <stl file> (optional)<dat file>")
    exit()

if (len(sys.argv) == 3):
    output_filename = sys.argv[2]
else:
    output_filename = os.path.splitext(sys.argv[1])[0] + ".dat"

mm_to_ldu = 1.0/0.4

with open(output_filename, "w") as fp_out:
    fp_out.write("0 " + output_filename + os.linesep)
    fp_out.write("0 !LDRAW Unofficial_part" + os.linesep)
    fp_out.write("0 BFC CERTIFY CCW" + os.linesep)

    with open(sys.argv[1]) as fp_in:
        number_triangles = 0
        triangle = ""
        for line in fp_in:
            if "vertex" in line:
                vertex = map(lambda x: (mm_to_ldu * float(x)), line.split()[1:])
                triangle += " {0:.3f} {1:.3f} {2:.3f}".format(*vertex)
            elif "endloop" in line:
                fp_out.write("3 16 " + triangle + os.linesep)
                triangle = ""
                number_triangles += 1

        print("Part contains", number_triangles, "triangles.")
        
