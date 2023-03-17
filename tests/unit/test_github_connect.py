from aws_cdk import (
    App,
    Stack,
    assertions
)

from special_octo_disco.github_connection import GithubConnection

def test_github_connection_construct():
    org = "test"
    repo = "repo"

    stack = Stack()

    GithubConnection(
        stack,
        "TestGithubConncention",
        github_org=org,
        github_repo=repo
    )

    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::IAM::Role", {
        "RoleName": f"{org}-{repo}-deploy"
    })