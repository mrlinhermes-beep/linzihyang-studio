# Cloudflare Pages Build Configuration

[build]
command = "echo 'Static site, no build needed'"
output_directory = "."

[[redirects]]
from = "/*"
to = "/index.php"
status = 200
