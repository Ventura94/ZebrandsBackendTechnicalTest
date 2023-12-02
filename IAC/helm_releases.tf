resource "helm_release" "ingress-nginx" {
  name       = "ingress-nginx"
  repository = "https://kubernetes.github.io/ingress-nginx"
  chart      = "ingress-nginx"
  namespace  = "ingress-nginx"
  set {
    name  = "controller.replicaCount"
    value = 1
  }
  set {
    name  = "controller.service.type"
    value = "LoadBalancer"
  }
  set {
    name  = "controller.metrics.enabled"
    value = true
  }
  set {
    name  = "controller.extraArgs.v"
    value = "2"
  }
  atomic           = true
  create_namespace = true
}

resource "helm_release" "cert-manager" {
  name             = "cert-manager"
  repository       = "https://charts.jetstack.io"
  chart            = "cert-manager"
  namespace        = "cert-manager"
  create_namespace = true
  set {
    name  = "installCRDs"
    value = true
  }
}

resource "helm_release" "postgresql" {
  name             = "zebrands-postgresql"
  repository       = "https://charts.bitnami.com/bitnami"
  chart            = "postgresql"
  namespace        = "zebrands-db"
  create_namespace = true

  set {
    name  = "volumePermissions.enabled"
    value = true
  }
  set_sensitive {
    name  = "global.postgresql.auth.postgresPassword"
    value = var.admin_postgres_password
  }
  set {
    name  = "global.postgresql.auth.username"
    value = "zebrands"
  }
  set_sensitive {
    name  = "global.postgresql.auth.password"
    value = var.zebrands_postgres_password
  }
  set {
    name  = "global.postgresql.auth.database"
    value = "zebrands"
  }
}
