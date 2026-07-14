"""
GCCS Trade Hunter - 本地 CORS 代理
用于让浏览器能调用不支持 CORS 的 API（如 GLM 智谱、MiniMax）

使用方法：
  python proxy.py            # 默认端口 8777
  python proxy.py 9000       # 指定端口

然后在 UI 的"CORS 代理 URL"填：http://localhost:8777/?url=

原理：浏览器 → 本代理 → 目标 API（绕过浏览器 CORS 限制）
Key 只经过你本机，不经过任何第三方。
"""
import http.server
import urllib.request
import urllib.parse
import sys
import json

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def _proxy(self):
        # 从 query 取目标 URL
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        target_url = params.get('url', [None])[0]

        if not target_url:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'missing ?url= parameter'}).encode())
            return

        # 读取请求 body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else None

        # 构造转发请求的 headers（保留 Authorization, Content-Type 等）
        forward_headers = {}
        for k, v in self.headers.items():
            k_lower = k.lower()
            # 跳过 hop-by-hop 和 host 头
            if k_lower in ('host', 'connection', 'accept-encoding', 'transfer-encoding'):
                continue
            forward_headers[k] = v

        # 发起转发请求
        req = urllib.request.Request(target_url, data=body, method=self.command, headers=forward_headers)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                resp_body = resp.read()
                self.send_response(resp.status)
                # 透传响应头（保留 content-type 等）
                for k, v in resp.headers.items():
                    if k.lower() in ('transfer-encoding', 'connection', 'content-encoding'):
                        continue
                    self.send_header(k, v)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', '*')
                self.end_headers()
                self.wfile.write(resp_body)
        except urllib.error.HTTPError as e:
            resp_body = e.read()
            self.send_response(e.code)
            for k, v in e.headers.items():
                if k.lower() in ('transfer-encoding', 'connection', 'content-encoding'):
                    continue
                self.send_header(k, v)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.end_headers()
            self.wfile.write(resp_body)
        except Exception as e:
            self.send_response(502)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def do_GET(self): self._proxy()
    def do_POST(self): self._proxy()
    def do_PUT(self): self._proxy()
    def do_DELETE(self): self._proxy()

    def do_OPTIONS(self):
        # 预检请求直接放行
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def log_message(self, fmt, *args):
        # 简化日志
        sys.stderr.write("[proxy] %s - %s\n" % (self.command, self.path.split('?')[0]))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8777
    server = http.server.HTTPServer(('127.0.0.1', port), ProxyHandler)
    print(f"\n  GCCS Local CORS Proxy")
    print(f"  ─────────────────────────────────────────")
    print(f"  Listening:  http://127.0.0.1:{port}")
    print(f"  Usage:      在 UI 的'CORS 代理 URL'填:")
    print(f"              http://localhost:{port}/?url=")
    print(f"  ─────────────────────────────────────────")
    print(f"  按 Ctrl+C 停止\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  代理已停止")
        server.server_close()


if __name__ == '__main__':
    main()
