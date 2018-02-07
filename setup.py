from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

setup(name='docker-bash-volume-watcher',
      version='1.0.8',
      packages=find_packages(),
      entry_points={
          'console_scripts': ['docker-volume-watcher=docker_volume_watcher.cli:main'],
          },
      description='A tool to notify Docker contianers about changes in mounts on Bash for Windows.',
      author='Kilian Volb, Mikhail Erofeev',
      author_email='kilian@nexus-stats.com',
      url='https://github.com/Kaptard/docker-bash-volume-watcher',
      install_requires=[
        'watchdog>=0.8.3',
        'docker==2.7.0',
        ],
      license='MIT',
      long_description=long_description,
      keywords='Docker volume Windows watch inotify',
      classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: System :: Monitoring'
        ],
  )
