from chalice import Chalice

app = Chalice(app_name='helloworld')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/sum')
def get_sum():
    args = app.current_request
    num1 = int(args.query_params['num1'])
    num2 = int(args.query_params['num2'])
    return {"sum": sum([num1, num2])}


@app.lambda_function()
def foo(event, context):
    return {"hello": "world"}

@app.lambda_function()
def bar(event, context):
    return {'event': event}
