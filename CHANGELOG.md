# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added
- `jobs_runs_wait_for_completion` flow - [#22](https://github.com/PrefectHQ/prefect-databricks/pull/22).

### Changed

- Migrate lines from `jobs_runs_submit_and_wait_for_completion` into `jobs_runs_wait_for_completion` flow - [#22](https://github.com/PrefectHQ/prefect-databricks/pull/22).

### Deprecated

### Removed

### Fixed

### Security

## 0.1.2

Released on TBD

### Added

- Logging of job runs tasks status within `jobs_runs_submit_and_wait_for_completion` - [#16](https://github.com/PrefectHQ/prefect-databricks/pull/16).

### Fixed

- Executing Python scripts through `jobs_runs_submit_and_wait_for_completion` - [#16](https://github.com/PrefectHQ/prefect-databricks/pull/16).


## 0.1.1

Released on August 19th, 2022.

### Added

- `jobs_runs_submit_and_wait_for_completion` flow - [#14](https://github.com/PrefectHQ/prefect-databricks/pull/14)

## 0.1.0

Released on August 15th, 2022.

### Added

- `execute_endpoint` and `jobs*` tasks - [#6](https://github.com/PrefectHQ/prefect-databricks/pull/6)
