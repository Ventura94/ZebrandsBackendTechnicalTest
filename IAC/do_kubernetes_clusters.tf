resource "digitalocean_kubernetes_cluster" "zebrands_kubernetes_service" {
  name         = "zebrands-services"
  region       = var.do_region
  version      = "1.28.2-do.0"
  auto_upgrade = true

  node_pool {
    name       = "zebrands-services-pool"
    size       = "s-2vcpu-4gb"
    auto_scale = true
    min_nodes  = 1
    max_nodes  = 4
  }
}