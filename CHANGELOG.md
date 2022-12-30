# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## 0.1.4

Released on December 30th, 2022.

### Fixed

- Type annotations in `jobs_runs_submit_and_wait_for_completion` and allowing `run_name=None` in `jobs_runs_wait_for_completion` flows - [#32](https://github.com/PrefectHQ/prefect-databricks/pull/32).
- Serialization of ACL permission objects and `AccessControlRequest` - [#49](https://github.com/PrefectHQ/prefect-databricks/issues/49).

## 0.1.3

Released on September 23rd, 2022.

### Fixed

- All models from the schema are now regenerated - [#29](https://github.com/PrefectHQ/prefect-databricks/pull/29).

## 0.1.2

Released on September 21st, 2022.

### Added

- Logging of job runs tasks status within `jobs_runs_submit_and_wait_for_completion` - [#16](https://github.com/PrefectHQ/prefect-databricks/pull/16).
- `jobs_runs_wait_for_completion` flow - [#22](https://github.com/PrefectHQ/prefect-databricks/pull/22).

### Changed

- Migrate lines from `jobs_runs_submit_and_wait_for_completion` into `jobs_runs_wait_for_completion` flow - [#22](https://github.com/PrefectHQ/prefect-databricks/pull/22).

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
