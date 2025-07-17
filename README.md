# MinIO High Availability (HA) CDN Setup using Docker and Nginx

This project sets up a **High Availability (HA)** MinIO cluster with NGINX acting as a reverse proxy and CDN. It supports load-balanced MinIO instances, public and private bucket access, and efficient file distribution.

## 🔧 Stack Overview

- **MinIO (x4 instances)** – Distributed object storage.
- **NGINX** – Acts as a reverse proxy. Also a CDN for public assets (images, videos, SVGs).
- **Docker Compose** – Container orchestration.
- **Public/Private Buckets** – Configurable access levels with optional caching for public assets.


## 🚀 Getting Started

### 1. Clone the Repo
```bash
cd minio-ha-cdn-setup
docker-compose up -d
```
To access MinIO console: `http://localhost:9001`


## ⚙️ Configuration

### ✅ NGINX

* Load balancing across MinIO nodes using `least_conn`
* Caching for public download endpoints (`/api/v1/buckets/.../objects/download`)
* Supports SVG, video, image types
* Configurable cache size and expiration  
* 🔍 Breakdown:
    - `max_size=1g`: Maximum size of the cache on disk.
    - `inactive=24h`: Cached content is removed if not accessed within 24 hours.
    - `proxy_cache_valid 200 1h`: Cache successful (200 OK) responses for 1 hour.
    - `proxy_cache_use_stale`: Serves stale content if the upstream is slow or fails (500/502/503/504).
    - `proxy_buffering on`: Enables response buffering, reducing disk I/O for repeated requests.
    - `proxy_cache_methods GET`: Only GET requests are cached.


### ✅ MinIO

* 4 distributed instances using erasure coding
* Configurable public/private bucket access
* Replication-ready setup

## 🔐 Bucket Access Model

| Bucket Type | Access        | Caching |
| ----------- | ------------- | ------- |
| `public`    | Public Read   | ✅ Yes   |
| `private`   | Authenticated | ❌ No    |

Manage access policies via the **MinIO Console** or `mc` CLI.

## 📦 Environment Notes

* All MinIO instances are assumed to run on the same machine (`localhost`) for dev/testing.
* Replace `localhost` with internal/external IPs for distributed deployment.

## ✅ To Do

* [ ] Add TLS support for production
* [ ] Enable MinIO bucket replication
* [ ] Add health check for backend failover