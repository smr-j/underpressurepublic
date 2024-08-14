# Terraform configuration
variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
  default     = "measurements-bucket"  
}

variable "tags" {
  description = "Tags to apply to the S3 bucket"
  type        = map(string)
  default     = {}
}
