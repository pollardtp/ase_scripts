import os, tarfile

# req: python3, everything else is downloaded into a file .tinker_ in the `cwd`

os.system('mkdir -p .tinkerrepo')

print('Downloading Ponder Tinker and dynamic_omm packages.')

# get
os.system('wget -nv --no-check-certificate https://tinyurl.com/ybbkzs54 -O .tinkerrepo/dynamic_omm.tar.gz') # dynamic_omm
os.system('wget -nv --no-check-certificate https://tinyurl.com/y7n7y4ov -O .tinkerrepo/tinker.8.5.2.tar.gz') # tinker 8.5.2

# unpack
tardyn_ = tarfile.open(".tinkerrepo/dynamic_omm.tar.gz")
tardyn_.extractall()
tartink_ = tarfile.open(".tinkerrepo/tinker.8.5.2.tar.gz")
tartink_.extractall()

# clean
os.system('mv openmm .tinkerrepo/dynamic_omm') # important if this is done a second time
os.system('mv tinker .tinkerrepo/tinker.8.5.2')
os.system('rm .tinkerrepo/dynamic_omm.tar.gz .tinkerrepo/tinker.8.5.2.tar.gz')

print('Downloading OpenMM-Tinker, OpenMM, and Tinker HP from Github, needs git --version > 1.19 for TLS 1.2.')

# get
os.system('git clone --progress https://github.com/pandegroup/openmm.git .tinkerrepo/openmm')
os.system('git clone --progress https://github.com/TinkerTools/Tinker-OpenMM.git .tinkerrepo/tinker-openmm')
os.system('git clone --progress https://github.com/TinkerTools/Tinker-HP.git .tinkerrepo/tinker-hp')

# set permissions, default is 777 less umask 037 (i.e., 740)
os.system('chmod 740 .tinkerrepo/openmm .tinkerrepo/tinker-openmm .tinkerrepo/tinker-hp .tinkerrepo/tinker.8.5.2 .tinkerrepo/dynamic_omm')

# next steps...
print('Next steps are to download newest versions of CMake and SWIG, ideally using conda3.')
print('As so: conda install -c anaconda cmake swig')

