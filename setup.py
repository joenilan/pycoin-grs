#!/usr/bin/env python

from setuptools import setup

from pycoin_grs.version import version

setup(
    name="pycoin_grs",
    version=version,
    packages=[
        "pycoin_grs",
        "pycoin_grs.blockchain",
        "pycoin_grs.cmds",
        "pycoin_grs.coins",
        "pycoin_grs.contrib",
        "pycoin_grs.convention",
        "pycoin_grs.ecdsa",
        "pycoin_grs.ecdsa.native",
        "pycoin_grs.key",
        "pycoin_grs.message",
        "pycoin_grs.networks",
        "pycoin_grs.serialize",
        "pycoin_grs.services",
        "pycoin_grs.tx",
        "pycoin_grs.tx.pay_to",
        "pycoin_grs.tx.script",
        "pycoin_grs.wallet"
    ],
    author="Richard Kiss",
    entry_points={
        'console_scripts':
            [
                'block = pycoin_grs.cmds.block:main',
                'ku = pycoin_grs.cmds.ku:main',
                'tx = pycoin_grs.cmds.tx:main',
                'msg = pycoin_grs.cmds.msg:main',
                # these scripts are obsolete
                'genwallet = pycoin_grs.cmds.genwallet:main',
                'spend = pycoin_grs.cmds.spend:main',
                'bu = pycoin_grs.cmds.bitcoin_utils:main',
            ]
        },
    author_email="",
    url="https://bitbucket.com/creativecrypto/pycoin_grs",
    license="http://opensource.org/licenses/MIT",
    description="Utilities for Bitcoin and altcoin addresses and transaction manipulation.",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],)
