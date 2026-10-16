output "api_base_url" {
  description = "Base URL for the API Gateway endpoint"
  value       = aws_apigatewayv2_api.lambda_api.api_endpoint
}
