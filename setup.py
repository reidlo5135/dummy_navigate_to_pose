from setuptools import setup

package_name: str = 'dummy_navigate_to_pose'
node_package_name: str = package_name + '.node'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name, node_package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='reidlo',
    maintainer_email='naru5135@wavem.net',
    description='ROS2(foxy) dummy navigate_to_pose action server package',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "dummy_navigate_to_pose = dummy_navigate_to_pose.main:main"
        ],
    },
)
