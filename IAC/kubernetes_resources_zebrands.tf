resource "kubernetes_namespace_v1" "zebrands_namespaces_services" {
  metadata {
    name = "zebrands-services"
  }
}


resource "kubernetes_secret_v1" "zebrands_services_environments_vars" {
  metadata {
    name      = "zebrands-service-environments-vars"
    namespace = kubernetes_namespace_v1.zebrands_namespaces_services.metadata.0.name
  }
  data = {
    DEBUG          = false
    DOCS_URL       = "/docs"
    OPENAPI_URL    = "/openapi.json"
    POSTGRESQL_URL = "postgresql://zebrands:${var.zebrands_postgres_password}@zebrands-postgresql.zebrands-db.svc.cluster.local:5432/zebrands"
    SECRET_KEY     = var.secret_key
    MAIL_USERNAME  = var.service_email
    MAIL_PASSWORD  = var.mail_password
    MAIL_FROM      = var.service_email
    MAIL_PORT      = 587
    MAIL_SERVER    = "smtp.gmail.com"
    MAIL_TLS       = true
    MAIL_SSL       = false
  }
  type = "Opaque"
}

resource "kubernetes_deployment_v1" "zebrands_services_deployment" {
  metadata {
    name      = "zebrands-services"
    namespace = kubernetes_namespace_v1.zebrands_namespaces_services.metadata.0.name
    labels    = {
      app = "zebrands-services"
    }
  }
  spec {
    revision_history_limit = 3
    replicas               = 1
    selector {
      match_labels = {
        app = "zebrands-services"
      }
    }
    template {
      metadata {
        labels = {
          app = "zebrands-services"
        }

      }
      spec {
        container {
          name  = "container-zebrands-services"
          image = "v3n2r4/zebrands_test:latest"
          resources {
            limits = {
              cpu    = "200m"
              memory = "512Mi"
            }
            requests = {
              cpu    = "100m"
              memory = "256Mi"
            }
          }
          readiness_probe {
            initial_delay_seconds = 10
            period_seconds        = 3
            http_get {
              path = "/"
              port = 8000
            }
          }
          liveness_probe {
            initial_delay_seconds = 10
            period_seconds        = 3
            http_get {
              path = "/"
              port = 8000
            }
          }
          env_from {
            secret_ref {
              name = kubernetes_secret_v1.zebrands_services_environments_vars.metadata.0.name
            }
          }
          port {
            container_port = 8000
          }
        }
      }
    }
  }
}


resource "kubernetes_service_v1" "zebrands_service_expose" {
  metadata {
    name      = "zebrnads-service-expose"
    namespace = kubernetes_namespace_v1.zebrands_namespaces_services.metadata.0.name
  }
  spec {
    type     = "ClusterIP"
    selector = {
      app = kubernetes_deployment_v1.zebrands_services_deployment.metadata.0.name
    }
    port {
      port        = 8000
      target_port = 8000
    }
  }
}


resource "kubernetes_secret_v1" "zebrands_digitalocean_dns_vars" {
  metadata {
    name      = "digitalocean-dns"
    namespace = kubernetes_namespace_v1.zebrands_namespaces_services.metadata.0.name
  }
  data = {
    access-token = var.do_token
  }
  type = "Opaque"
}

resource "kubernetes_manifest" "zebrands_services_cert_issuer" {
  manifest = {
    apiVersion = "cert-manager.io/v1"
    kind       = "Issuer"
    metadata   = {
      name      = "letsencrypt-nginx"
      namespace = kubernetes_namespace_v1.zebrands_namespaces_services.metadata.0.name
    }
    spec = {
      acme = {
        email               = var.maintainer_email
        server              = "https://acme-v02.api.letsencrypt.org/directory"
        privateKeySecretRef = {
          name : "letsencrypt-nginx-private-key"
        }
        solvers = [
          {
            dns01 = {
              digitalocean = {
                tokenSecretRef = {
                  name = kubernetes_secret_v1.zebrands_digitalocean_dns_vars.metadata.0.name
                  key  = "access-token"
                }
              }
            }
          }
        ]
      }
    }
  }
}

resource "kubernetes_ingress_v1" "zebrands_services_ingress" {
  depends_on             = [helm_release.ingress-nginx]
  wait_for_load_balancer = true
  metadata {
    name        = "zebrands-services-ingress"
    namespace   = kubernetes_namespace_v1.zebrands_namespaces_services.metadata.0.name
    annotations = {
      "cert-manager.io/issuer"                     = "letsencrypt-nginx",
      "nginx.ingress.kubernetes.io/enable-real-ip" = true,
      "nginx.ingress.kubernetes.io/real-ip-header" = "proxy_protocol"
      "nginx.ingress.kubernetes.io/limit-rps"      = "10"
    }
  }
  spec {
    ingress_class_name = "nginx"
    tls {
      hosts       = [digitalocean_record.zebrand_record_ipv4.fqdn,]
      secret_name = "letsencrypt-nginx"
    }
    rule {
      host = digitalocean_record.zebrand_record_ipv4.fqdn
      http {
        path {
          path = "/"
          backend {
            service {
              name = kubernetes_service_v1.zebrands_service_expose.metadata.0.name
              port {
                number = 8000
              }
            }
          }
        }
      }
    }
  }
}