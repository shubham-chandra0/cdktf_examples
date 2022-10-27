#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws import provider,dynamodb_table,opensearch_domain

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        provider.AwsProvider(self,"AWS",region="us-east-1")
        """
        Setting replica to different region other than the providers region will convert the regular DynamoDB Table to Global table (here replication will be available on east1 and east2)
        """
        dynamodb_1 = dynamodb_table.DynamodbTable(self,"myDynamoTable1",
                                                name="myTable1",attribute=[{"name":"id","type":"S"}],
                                                hash_key="id",stream_enabled=True,
                                                stream_view_type = "NEW_AND_OLD_IMAGES",
                                                replica=[{"regionName":"us-east-2"}],
                                                billing_mode="PAY_PER_REQUEST",
                                                server_side_encryption={"enabled":True})


        opensearch_domain.OpensearchDomain(self,"Domain",
                                        domain_name="trialdomain", 
                                        cluster_config={"instance_type":"i3.large.search","instance_count":3},
                                        #ebs_options={"ebs_enabled":True,"volume_size":10},
                                        advanced_security_options={"enabled":True,"internal_user_database_enabled":True,"master_user_options":{"master_user_name":"demo","master_user_password":"Demo@1234"}},
                                        node_to_node_encryption={"enabled":True},
                                        encrypt_at_rest={"enabled":True},
                                        domain_endpoint_options={"enforce_https":True,"tls_security_policy":"Policy-Min-TLS-1-0-2019-07"},
                                        #log_publishing_options=[{"cloudwatchLogGroupArn":"arn:aws:logs:us-east-1:216189934404:*","logType":"INDEX_SLOW_LOGS","enabled":True}],
                                        depends_on=[dynamodb_1])


app = App()
MyStack(app, "cdktf_app")

app.synth()
