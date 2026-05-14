# 403 Bypasser

A Python-based security testing tool designed to evaluate alternative response behaviors when a target endpoint returns **HTTP 403 Forbidden**.

> ⚠️ For educational purposes and authorized security testing only.

---

## 📌 Overview

`403bypasser.py` performs automated checks against a specified target URL to determine whether different request techniques result in responses other than `403 Forbidden`.

The tool tests multiple vectors including:

- HTTP method variations
- IP header manipulation
- Path manipulation
- Case sensitivity checks
- Header override attempts
- Basic path race condition behavior

---

## 🚀 Features

### 1️⃣ HTTP Method Testing
Tests multiple HTTP methods such as:

- `GET`
- `POST`
- `PUT`
- `DELETE`
- `PATCH`
- `OPTIONS`
- `HEAD`
- `TRACE`
- `CONNECT`
- `PROPFIND`
- `MOVE`

If a method returns a status code other than `403`, it is displayed.

---

### 2️⃣ IP Header Manipulation

Tests different IP-related headers including:

- `X-Forwarded-For`
- `X-Real-IP`
- `X-Originating-IP`
- `X-Client-IP`
- `X-Remote-IP`
- `X-Remote-Addr`
- `X-Custom-IP-Authorization`

Each header is tested against multiple IP formats:
- `127.0.0.1`
- `localhost`
- Decimal representation (`2130706433`)
- Hex representation (`0x7F000001`)
- Alternative IPv4 formats

---

### 3️⃣ Path Manipulation Testing

Appends multiple variations to the target path including:

- Encoded dot sequences (`%2e`)
- Encoded slash variations
- Null byte patterns
- Multiple slashes
- File extensions (`.json`, `.css`, `.html`)
- Query parameter mutations
- Fragment identifiers

If a response differs from 403, the tool prints:
- Status code
- Content length
- Response time

---

### 4️⃣ Case Sensitivity Testing

Tests:
- Uppercase path
- Title case path
- Per-character case mutation

Useful for environments with case-sensitive file systems.

---

### 5️⃣ Header Override Testing

Tests headers such as:

- `X-Original-URL`
- `X-Rewrite-URL`
- `X-Forwarded-Host`
- `X-Forwarded-For`

---

## 🛠 Requirements

- Python 3.8+
- `requests`
- `pyinputplus`

Install dependencies:

```bash
pip install requests pyinputplus
OR
pip install -r requirements.txt
```
---
## ▶ Usage

Run the script:

python3 403bypasser.py

Enter a target URL in the format:

https://example.com/admin
https://example.com/path/to/resource

The script validates input using a regex pattern.
---
## 🧪 Example Output
[*] HTTP method bypass starting...

POST method with 200 code is possible for bypass

[*] HTTP method bypass finished.

[*] IP bypass starting...
X-Forwarded-For with 127.0.0.1 is possible for bypass

---
## ⚠️ Important Notes

The script flags any response where status_code != 403.

A different status code does not automatically mean a successful bypass.

Always verify response content and behavior manually.

Network instability may cause timeouts.

Some techniques may not apply depending on server configuration.

----

### Do NOT use this tool against systems without explicit permission.
---
## 👨‍💻 Author
# THXY
Cybersecurity Student | Python Learner
---
