from setuptools import setup, find_packages

setup(
    name='latent-diffusion',
    version='0.0.2',
    description='',
    packages=["ldm"],
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
