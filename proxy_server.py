from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return "Missing URL", 400

    try:
        r = requests.get(target_url)
        html = r.text

        terms = ["rhinoceros", "Rhinoceros", "Rhinoceri", "rhinos", "Rhinos", "rhino", "Rhino"]
        for t in terms:
            html = html.replace(t, "fat, gray unicorn")

        return Response(html, content_type=r.headers.get("Content-Type", "text/html"))
    except:
        return "Something went wrong", 500

if __name__ == '__main__':
    app.run(port=5000)
