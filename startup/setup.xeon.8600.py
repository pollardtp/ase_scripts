import os, sys

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

os.system('wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh')
print('Install conda, then run `conda install git`')

os.system('wget http://fftw.org/fftw-3.3.8.tar.gz')
print('Install via typical ./configure --prefix=`pwd` --enable-threads --enable-mpi, make CFLAGS="-O3 -xHost", make install, and add to LD_LIBRARY_PATH')

#os.system('git clone https://github.com/TinkerTools/Tinker-HP.git')
#os.system('mv Tinker-HP tinkerhp.1.0')
print('Once you have conda installed, uncomment the two lines above (see source) and comment out the previous download commands, but it is not essential.')
print('cd tinkerhp1.0/v1.0/2decomp_fft/src; edit Makefile.inc to change paths and change FFT to fftw from whatever it is by default.')

