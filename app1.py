
from flask import Flask
from flask import url_for
print("a")
app=Flask(__name__)

@app.route("/")
def hello():
	return 'Hello'

@app.route("/user/<name>")
def user_page(name):
	return 'User: %s' % name

@app.route("/test")
def test_url_for():
	print(url_for("hello"))
	print(url_for("user_page",name="cense"))
	print(url_for("test_url_for"))
	print(url_for('test_url_for',num=2))
	print("a")
	return 'Test page'