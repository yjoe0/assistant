# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import platform

system = platform.system()
if system == 'Windows':
    install_requires = ['PyAudio', 'mp3play','numpy','requests']
elif system == 'Linux':
    install_requires = ['PyAudio', 'mpg123','numpy','requests']
setup(
      name="assistant",
      version="0.10",
      description="百度语音、图灵机器人结合PyAudio制作的国内对话机器人",
      author="yjoe0",
      url="https://github.com/yjoe0/assistant/tree/class",
      license="LGPL",
      packages= find_packages(),
      install_requires = install_requires

)