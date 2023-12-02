resource "digitalocean_record" "zebrand_record_ipv4" {
  domain = digitalocean_domain.zebrands_domain.name
  type   = "A"
  name   = "zebrands"
  value  = "138.197.231.95"
  ttl    = 30
}

