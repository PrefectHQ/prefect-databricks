# generated by datamodel-codegen:
#   filename:  repos-2.0-aws.yaml
#   timestamp: 2022-06-29T19:47:39+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Error(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    error_code: Optional[str] = Field(None, description='Error code')
    message: Optional[str] = Field(
        None,
        description='Human-readable error message describing the cause of the error.',
    )


class Branch(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: str = Field(
        ...,
        description='Branch that the local version of the repo is checked out to.',
        example='main',
    )


class HeadCommitId(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: str = Field(
        ...,
        description=(
            'SHA-1 hash representing the commit ID of the current HEAD of the repo.'
        ),
        example='7e0847ede61f07adede22e2bcce6050216489171',
    )


class Id(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: int = Field(
        ...,
        description='ID of the repo object in the workspace.',
        example=5249608814509279,
    )


class NextPageToken(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: str = Field(
        ...,
        description=(
            'Token that can be specified as a query parameter to the GET /repos'
            ' endpoint to retrieve the next page of results.'
        ),
        example='eyJyZXBvX3RyZWVub2RlX2lkIjo1MjQ5NjA4ODE0NTA5Mjc5fQ==',
    )


class Path(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: str = Field(
        ...,
        description=(
            'Desired path for the repo in the workspace. Must be in the format'
            ' /Repos/{folder}/{repo-name}.'
        ),
        example='/Repos/Production/testrepo',
    )


class Provider(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: str = Field(
        ...,
        description=(
            'Git provider. This field is case-insensitive. The available Git providers'
            ' are gitHub, bitbucketCloud, gitLab, azureDevOpsServices,'
            ' gitHubEnterprise, bitbucketServer, gitLabEnterpriseEdition and'
            ' awsCodeCommit.'
        ),
        example='gitHub',
    )


class Tag(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: str = Field(
        ...,
        description=(
            'Tag that the local version of the repo is checked out to. Updating the'
            ' repo to a tag puts the repo in a detached HEAD state. Before committing'
            ' new changes, you must update the repo to a branch instead of the detached'
            ' HEAD.'
        ),
        example='v1.0',
    )


class Url(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    __root__: str = Field(
        ...,
        description='URL of the Git repository to be linked.',
        example='https://github.com/jsmith/test',
    )


class BranchModel(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    branch: Branch


class CreateRepoRequest(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    path: Optional[Path] = None
    provider: Provider
    url: Url


class GetRepoResponse(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    branch: Optional[Branch] = None
    head_commit_id: Optional[HeadCommitId] = None
    id: Optional[Id] = None
    path: Optional[Path] = None
    provider: Optional[Provider] = None
    url: Optional[Url] = None


class GetReposResponse(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    next_page_token: Optional[NextPageToken] = None
    repos: Optional[List[GetRepoResponse]] = None


class TagModel(BaseModel, extra=Extra.allow):
    class Config:
        allow_mutation = False

    tag: Tag
