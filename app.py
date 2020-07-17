#!/usr/bin/env python3

from aws_cdk import core

from cdkteht3.cdkteht3_stack import Cdkteht3Stack


app = core.App()
Cdkteht3Stack(app, "cdkteht3", env={'region': 'us-west-2'})

app.synth()