## Status

| Bintray | Linux/macOS |
|:--------:|:-----------------:|
|[![Download](https://api.bintray.com/packages/morheit/conan/folly%3Amorheit/images/download.svg)](https://bintray.com/morheit/conan/folly%3Amorheit/2019.11.11.00%3Astable)|[![Build Status](https://travis-ci.org/Morheit/conan-folly.svg?branch=stable%2F2019.11.11.00)](https://travis-ci.org/Morheit/conan-folly)|

## Conan Recipe for [*Folly*](https://github.com/facebook/folly)

Folly (acronymed loosely after Facebook Open Source Library) is a library of C++14 components.

The packages generated with conanfile from this repository can be found on [Bintray](https://bintray.com/morheit/conan/folly%3Amorheit/).

## Setup

### Basic Setup

    $ conan remote add conan-morheit https://api.bintray.com/conan/morheit/conan
    $ conan install folly/2019.11.11.00@morheit/stable

### Project Setup

For project setup specify the package in your *conanfile.txt*
```
[requires]
folly/2019.11.11.00@morheit/stable

[generators]
cmake
```
