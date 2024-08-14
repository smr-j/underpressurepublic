
resource "aws_s3_bucket" "s3_bucket" {
  bucket = var.bucket_name
  tags   = var.tags
}


resource "aws_s3_bucket_acl" "s3_bucket" {
  bucket = aws_s3_bucket.s3_bucket.id
  acl    = "public-read"
}


# resource "aws_s3_object" "object_assets" {
#   depends_on = [aws_s3_bucket.s3_bucket]
#   for_each   = fileset(path.module, "assets/*")
#   bucket     = var.bucket_name
#   key        = each.value
#   source     = "${each.value}"
#   etag       = filemd5("${each.value}")
#   acl        = "public-read"
# }

resource "aws_s3_bucket_policy" "s3_bucket" {
  bucket = aws_s3_bucket.s3_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource = [
          aws_s3_bucket.s3_bucket.arn,
          "${aws_s3_bucket.s3_bucket.arn}/*",
        ]
      },
    ]
  })
}