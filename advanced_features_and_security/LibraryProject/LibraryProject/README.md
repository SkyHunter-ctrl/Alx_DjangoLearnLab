# This  a NEW Django bee
Let do it hunter
## HTTPS Security Configuration

- `SECURE_SSL_REDIRECT`: Forces HTTPS for all requests
- `SECURE_HSTS_SECONDS`: Instructs browsers to enforce HTTPS for 1 year
- `SESSION_COOKIE_SECURE` & `CSRF_COOKIE_SECURE`: Cookies only sent over HTTPS
- `X_FRAME_OPTIONS`: Prevents clickjacking
- `SECURE_CONTENT_TYPE_NOSNIFF`: Blocks MIME-type sniffing
- `SECURE_BROWSER_XSS_FILTER`: Enables browser XSS protection

## Deployment Notes

- SSL/TLS configured via Nginx with Let's Encrypt
- Certbot used for certificate issuance and auto-renewal
- CSP headers recommended for further XSS protection