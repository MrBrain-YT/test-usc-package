from flask import Flask, render_template


def test(app:Flask):
    
    @app.route('/test/', methods = ['GET'])
    def test_site():
        return render_template("test/test.html")
    
    
if __name__ == "__main__":
    app = Flask(__name__)
    test(app)
