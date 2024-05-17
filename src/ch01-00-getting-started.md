# Getting Started
Patrician 3 is a 32bit executable with no DRM or anti debugging methods included.
Reverse engineering suites such as [IDA](https://hex-rays.com/ida-free/) or [Ghidra](https://ghidra-sre.org/) can decompile most functions.
While some classes have vtables, most functions operate on structs, and the call hierarchy can be analyzed statically.

## Scripts and Tooling
Sometimes, this book will provide [IDC scripts](https://www.hex-rays.com/products/ida/support/idadoc/157.shtml) that help debugging and understanding Patrician 3's runtime behavior.
A Cheat Engine table can be found in the appendix.
There is also a [Rust library](https://github.com/P3Modding/p3-lib) that provides an API to Patrician 3's memory space.

## Abbreviations
| Abbreviation | Meaning     |
|--------------|-------------|
| P3           | Patrician 3 |
