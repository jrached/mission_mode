import os
from glob import glob
from setuptools import setup
  
package_name = 'mission_mode'  
setup(
    name=package_name,
    version='0.0.0',
    # packages=['rqt_pkg'],
    packages=[package_name],
    # package_dir={'': 'src'},
    install_requires=['setuptools'],
    tests_require=['pytest'],
    zip_safe=True,
    maintainer='Brett',
    maintainer_email='brett@todo.todo',
    description='GUI for selecting global flight mode',
    license='MIT',
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('resource/*')),
        (os.path.join('share', package_name), ['plugin.xml']),
        (os.path.join('share', package_name, 'cfg'), ['cfg/default.perspective']),
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)

