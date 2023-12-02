variable "do_token" {
  sensitive = true
  type      = string
}

variable "do_region" {
  type    = string
  default = "nyc1"
}

variable "maintainer_email" {
  type    = string
  default = "arianventura94@gmail.com"
}

variable "zebrands_postgres_password" {
  sensitive = true
  type      = string
}
variable "admin_postgres_password" {
  sensitive = true
  type      = string
}

variable "secret_key" {
  sensitive = true
  type      = string
}

variable "service_email" {
  type    = string
  default = "arianventura94@gmail.com"
}


variable "mail_password" {
  sensitive = true
  type      = string
}

variable "domain" {
  type = string
}




