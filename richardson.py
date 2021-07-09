import flask

data_in = ["1", "2", "3", "10", "11", "19", "20", "21", "100", "101", "150", "159", "1080", "0,1", "0,2", "0,264", "-0,1", "-0,2", "-0,264", "-1", "-2", "-3", "-10", "-11", "-12", "-18", "-19", "-20", "-21", "-100", "-101"]
data_out = ["2", "3", "4", "20", "21", "29", "30", "31", "200", "201", "250", "259", "2080", "0,2", "0,3", "0,364", "0", "-0,1", "-0,164", "0", "-1", "-2", "0", "-1", "-2", "-8", "-9", "-10", "-11", "0", "-1"]
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])

# example http://127.0.0.1:5000/?id=-1
# example http://127.0.0.1:5000/?id=0
# example http://127.0.0.1:5000/?id=-0,1

def get():
    id = flask.request.args.get('id')
    # check for 0
    if id == "0":
        return ("NOT ACCEPTABLE", 406)
    else:
        # check if the number value exist in data_in
        try:
            index = data_in.index(str(id))
        # if not then return an error "Error Wrong Number" with exit code 406
        except:
            return ("Error Wrong Number", 406)
        return (data_out[index], 200)

app.run()