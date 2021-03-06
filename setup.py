from distutils.core import setup, Extension

#extension = Extension('fenics_mpm', \
#                      ['fenics_mpm/cpp/MPMElasticMaterial.cpp', \
#                       'fenics_mpm/cpp/MPMImpenetrableMaterial.cpp', \
#                       'fenics_mpm/cpp/MPMMaterial.cpp', \
#                       'fenics_mpm/cpp/MPMModel.cpp'], \
#                      include_dirs=['fenics_mpm/cpp/'], \
#                      language="c++")


setup(  name        = 'fenics_mpm',
        version     = '1.0',
        description = 'MPM with FEniCS',
        author      = 'Evan M. Cummings',
        url         = 'https://github.com/pf4d/fenics_mpm',
        packages    = ['fenics_mpm'],
        package_dir = {'fenics_mpm' : 'fenics_mpm'})
        #ext_modules = extension)



