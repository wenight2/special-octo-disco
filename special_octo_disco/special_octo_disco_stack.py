from aws_cdk import (
    Duration,
    Stack,
    aws_apigateway as _api_gw,
    aws_lambda as _lambda,
    CfnOutput,
    aws_iam as iam,
)
from constructs import Construct
from special_octo_disco.github_connection import GithubConnection

class SpecialOctoDiscoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        the_lambda = _lambda.Function(self, id="thelamdbafunction",
                                    runtime=_lambda.Runtime.PYTHON_3_8,
                                    handler="index.handler", 
                                    code= _lambda.Code.from_asset(('lambdascript')))
        the_api_gw = _api_gw.LambdaRestApi(self, 
                                           id="therestapi", 
                                           rest_api_name="some2-api", 
                                           handler=the_lambda)
        # github_provider = iam.OpenIdConnectProvider(self, "GitHubProvider",
        #     url="https://token.actions.githubusercontent.com",
        #     client_ids=["sts.azazomaws-com"]
        # );
        
        # GithubConnection(self, "GithubDeploymentRole", 'wenight2', 'special-octo-disco')
        
        # CfnOutput(self, "GitHubProviderArn", value=github_provider.open_id_connect_provider_arn)