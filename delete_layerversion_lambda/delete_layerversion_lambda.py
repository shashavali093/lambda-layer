import json, boto3, logging
import cfnresponse
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
  logger.info("event: {}".format(event))
  client = boto3.client('lambda')
  try:
      layer = event['ResourceProperties']['LayerName']
      logger.info("layer: {}, event['RequestType']: {}".format(layer,event['RequestType']))
      
      if event['RequestType'] == 'Delete':
          for versions in client.list_layer_versions(LayerName=layer)['LayerVersions']:
              version_number=versions['Version']
              response = client.delete_layer_version(LayerName=layer,VersionNumber=version_number)

      sendResponseCfn(event, context, cfnresponse.SUCCESS)
  except Exception as e:
      logger.info("Exception: {}".format(e))
      sendResponseCfn(event, context, cfnresponse.FAILED)

def sendResponseCfn(event, context, responseStatus):
  responseData = {}
  responseData['Data'] = {}
  cfnresponse.send(event, context, responseStatus, responseData, "CustomResourcePhysicalID")