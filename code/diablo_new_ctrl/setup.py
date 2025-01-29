from setuptools import setup

package_name = 'diablo_new_ctrl'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sofia',
    maintainer_email='sofia.el-khalifi@insa-lyon.fr',
    description='Diablo publisher/subscriber',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = diablo_new_ctrl.diablo_publisher:main',
                'listener = diablo_new_ctrl.diablo_subscriber:main',
        ],
},
)
