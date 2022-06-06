# Shaker

A collection of Fedora packages for customizing Qubes OS with SaltStack.

## Overview

- [Introduction](#introduction)
- [Installation](#installation)
- [Thanks](#thanks)

## Introduction

This repository contains the files needed to build Fedora packages to manage the configuration of various Qubes OS VMs. See the `.spec` files for details about each package.

## Installation

The below steps will guide you through generating the Fedora packages from source. See the [RedHat docs](https://www.redhat.com/sysadmin/create-rpm-package) for more details.

### Tools

These tools should be installed on the machine you'll be building the packages on.

| Tool                                                      | Description                                              |
|-----------------------------------------------------------|----------------------------------------------------------|
| [rpmdevtools](https://fedoraproject.org/wiki/Rpmdevtools) | Contains many scripts to aid in RPM package development. |

This setup is done automatically you when you run `make setup`

### Building packages

1. Build the rpm packages
    - All packages can be built by running `make`
    - Individual packages can be built by running commands such as `make cacher`

1. Copy the rpm files from `rpmbuilder/RPMS` to your dom0 qube
    ```bash
    qvm-run --pass-io <src-vm> 'cat ~/rpmbuilds/RPMS/x86_64/aw-qubes-cacher-salt-1.5-1.fc34.x86_64.rpm' > aw-qubes-cacher-salt.rpm
    ```
    - WARNING: There are security risks when copying to dom0 and this process bypasses some of the usual security mechanisms of Qubes. Make sure to inspect this code before installing and review the [qubes docs on this subject](https://www.qubes-os.org/doc/how-to-copy-from-dom0/#copying-to-dom0).

1. Install the RPM packages in dom0
    ```bash
    sudo dnf install ~/aw-qubes-cacher-salt.rpm
    ```

## Thanks

These packages have been forked from those created by `[unman](https://github.com/unman/shaker).
A huge thank you to unman and the other maintainers of Qubes OS and its many dependencies.