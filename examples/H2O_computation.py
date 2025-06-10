try:
    import os, sys
    print(os.getcwd())
    sys.path.insert(1, os.path.abspath(f'{os.getcwd()}/../spool/stage/lib'))
except ImportError:
    pass

import psi4
psi4.set_memory('60000 MB')

h2o = psi4.geometry("""
0 1
Ar   0.000000   0.000000  -0.056437
Ar   0.000000   0.758602   0.447847
Ar   0.000000  -0.758602   0.447847
""")
print(h2o.save_string_xyz())


# SCF with a minimal basis set
psi4.set_options({
    'basis': 'aug-cc-pV5Z',
    'scf_type': 'pk',
    'reference': 'rhf'
})
# Optimize geometry and print final energy
energy = psi4.optimize('scf')
print("Optimized Energy (Hartree):", energy)

