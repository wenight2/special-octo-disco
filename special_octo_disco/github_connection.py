from aws_cdk import (
    aws_iam as iam,
    CfnOutput,
    Duration,
    App
)

from constructs import Construct

class GithubConnection(Construct):
    
    def __init__(self, scope: Construct, construct_id: str, github_org: str, github_repo: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        oidc_arn = f"arn:aws:iam::{App.account}:oidc-provider/token.actions.githubusercontent.com"
        
        provider = iam.OpenIdConnectProvider.from_open_id_connect_provider_arn(
            self,
            "GithubProvider",
            oidc_arn
        )

        principle = iam.OpenIdConnectPrincipal(provider).with_conditions(
            conditions={
                "StringLike": {
                    'token.action.githubusercontent.com:sub':
                        f'repo:{github_org}/{github_repo}:*'
                }
            }
        )

        principle.add_to_principal_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["sts:AssumeRoleWithWebIdentity"],
                resources=["*"]
            )
        )

        iam.Role(self, "DeploymentRole", 
            assumed_by=principle, 
            role_name=f"{github_org}-{github_repo}-deploy", 
            max_session_duration=Duration.seconds(3600), 
            inline_policies={
                "DeploymentPolicy": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=['sts:AssumeRole'],
                            effect=iam.Effect.ALLOW,
                            resources=[f'arn:aws:iam::{App.account}:role/cdk-*'],
                        )
                    ]
                )
            }
        )

        CfnOutput(self, "DeploymentRoleArn", value=f"arn:aws:iam::{App.account}:role/{github_org}-{github_repo}-deploy")