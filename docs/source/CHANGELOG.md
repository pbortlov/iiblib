# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- N/A

## [0.12.0] - 2020-09-29

### Added

 - added support for 'omps_operator_version'
  
### Changed

 - 'bundles' is now an optional parameter in IIB requests
 - 'binary_image' is now an optional parameter in IIB requests

## [0.11.0] - 2020-07-06

### Added

 - timout for getting build in final state (default 2 hours)
 - backoff factor for retrying data from API 
  
### Changed

 - retry is now triggered for all 5xx HTTP status codes (500-511)

## [0.10.0] - 2020-06-25

### Fixed

- usage in README
- default location for keytab

### Added

- support for "overwrite-from-index-token" when calling IIB

### Changed

- password-based auth to token by replacing content-delivery-release-bot

## [0.9.0] - 2020-03-30

### Added

- added overwrite_from_index param support

## [0.8.0] - 2020-03-04

### Changed

- better error reporting for IIB errors

### Added

- to_dict method for IIBBuildDetailsModel

## [0.7.0] - 2020-03-04

### Fixed

- rhel 6 compatibility kerberos fixes

## [0.6.0] - 2020-03-01

### Fixed

- requests-gssapi replaced with requests-kerberos

## [0.5.0] - 2020-02-29

### Fixed

- kerberos auth fixed

## [0.4.0] - 2020-02-27

### Fixed

- make client compatible with upstream IIB

## [0.3.0] - 2020-02-27

### Fixed

- Fixed kerberos auth
- added way how to configure insecure ssl connection to IIB

## [0.2.0] - 2020-02-26

### Fixed

- Fixed incompatibilities with IIB

## [0.1.0] - 2020-02-21

### Added
- First iiblib release with support of basic IIB operations
