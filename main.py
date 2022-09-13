from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    copy_n = n  
    order = len(str(n))
    sum = 0
    while n>0:
        digit = n%10
        sum += digit **order
        n =n//10

    if copy_n == sum:
        print("The given number", copy_n, "is armstrong number")
        result = {
            "Number" :n,
            "Armstrong" : True,
            "Server IP" : "122.234.213.53",
            "Other Numbers" : [1,23,45,5,3]
        }
    else:
        print("The given number", copy_n, "is not armstrong number")
        result = {
            "Number" :n,
            "Armstrong" : False,
            "Server IP" : "122.234.213.53",
            "Other Numbers" : [1,23,45,5,3]
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
    