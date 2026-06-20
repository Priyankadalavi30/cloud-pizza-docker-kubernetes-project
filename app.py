from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Pizza Factory</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ff9966, #ff5e62);
                color: white;
                text-align: center;
            }

            .container {
                margin-top: 100px;
            }

            h1 {
                font-size: 60px;
                margin-bottom: 10px;
            }

            h2 {
                font-size: 30px;
                margin-bottom: 20px;
            }

            .card {
                background: rgba(255,255,255,0.15);
                width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
            }

            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 25px;
                background: white;
                color: #ff5e62;
                text-decoration: none;
                border-radius: 30px;
                font-weight: bold;
                transition: 0.3s;
            }

            .btn:hover {
                background: #ffe6e6;
                transform: scale(1.05);
            }

            footer {
                margin-top: 80px;
                font-size: 14px;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <div class="card">
                <h1>🍕 Cloud Pizza Factory</h1>
                <h2>Fresh & Delicious Pizzas Delivered Fast</h2>

                <p>🔥 Today's Special</p>
                <h2>Paneer Tikka Pizza</h2>

                <p>🚀 Powered by Docker & Kubernetes</p>

                <a href="#" class="btn">Order Now</a>
            </div>

            <footer>
                © 2026 Cloud Pizza Factory | AWS DevOps Demo Project
            </footer>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)