#!/usr/bin/env python3
import os
from aws_cdk import core

from cdkteht3.cdkteht3_stack import Cdkteht3Stack

myenv = os.environ['AWS_ACCOUNTID']
app = core.App()
Cdkteht3Stack(app, "cdkteht3", env={'region': 'eu-west-1', 'account': myenv})

app.synth()
