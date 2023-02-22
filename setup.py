# ---------------------------------------------------------------------------------------------
#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(install_requires=requirements)
