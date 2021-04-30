import redis
from flask import Flask

conn = redis.Redis('localhost')

application = Flask(__name__)


@application.route("/health")
def health():
    return "Hello from CloudEnsure Internal API!"


@application.route("/<key>", methods=['GET'])
def find_key(key):
    try:
        print(key, type(key))
        values = conn.hgetall(key)
        x = {y.decode('ascii'): values.get(y).decode(
            'ascii') for y in values.keys()}

        return x
    except Exception as e:
        print(e)
        message = "No result Found"
    return message


if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')
