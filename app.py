#!/usr/bin/env python3
import os

import aws_cdk as cdk

from special_octo_disco.special_octo_disco_stack import SpecialOctoDiscoStack


app = cdk.App()
SpecialOctoDiscoStack(app, "SpecialOctoDiscoStack"
    )

app.synth()
