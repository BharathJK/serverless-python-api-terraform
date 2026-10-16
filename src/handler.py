import json


def lambda_handler(event, context):
  print("Received event: " + json.dumps(event))

  # Simple routing based on path
  path = event.get("rawPath", "/")

  if path == "/health":
    body = {"status": "healthy", "message": "Serverless Lambda API is running!"}
  else:
    body = {
        "message": "Welcome to your Serverless DevOps Portfolio API!",
        "endpoints": ["/health", "/data"],
    }

  return {
      "statusCode": 200,
      "headers": {"Content-Type": "application/json"},
      "body": json.dumps(body),
  }
