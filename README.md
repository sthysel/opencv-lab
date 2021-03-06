# Playing with OpenCV

![Peacocks](./pics/grab.jpg)

# Install OpenCV 4.0.1


Build from source to switch things on.

Get sources and prep build folders

```
$ mkdir ~/opencv
$ git clone -b 4.0.1 https://github.com/opencv/opencv.git opencv
$ cd opencv
$ git clone https://github.com/opencv/opencv_contrib.git opencv_contrib
$ mkdir release
$ cd release
```

make a virtualenv and drop lib in there

```
$ mkvirtualenv opencv-play
$ export VENV=~/.virtualenvs/opencv-play
$ export ARCH_BIN=
$ cmake -DCMAKE_INSTALL_PREFIX=${VENV} \
      -DCPYTHON_EXECUTABLE=${VENV}/bin/python \
      -DCPYTHON_PACKAGES_PATH=${VENV}/lib/python3.7/site-packages \
      -DCMAKE_BUILD_TYPE=RELEASE \
      -DINSTALL_PYTHON_EXAMPLES=ON \
      -DINSTALL_C_EXAMPLES=OFF \
      -DOPENCV_EXTRA_MODULES_PATH=~/opencv/opencv_contrib/modules \
      -DBUILD_PYTHON_SUPPORT=ON \
      -DWITH_XINE=ON -D WITH_OPENGL=ON \
      -DWITH_TBB=ON \
      -DWITH_EIGEN=ON \
      -DBUILD_EXAMPLES=ON \
      -DBUILD_NEW_PYTHON_SUPPORT=ON \
      -DWITH_V4L=ON \
      -DBUILD_EXAMPLES=ON \
      -DWITH_CUDA=ON \
      -DCUDA_ARCH_BIN=${ARCH_BIN} \
      -DCUDA_ARCH_PTX="" \
      -DCUDA_FAST_MATH=ON \
      -DWITH_CUBLAS=ON \ 
      ../
```

Build quicker

```
$ make -j4
$ make install
```

# Resources

 - https://docs.opencv.org/4.0.1/
