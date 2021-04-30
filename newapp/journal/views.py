import redis
from django.http import HttpResponse
from django.shortcuts import render
from io import StringIO
from csv import DictWriter
conn = redis.Redis('localhost')

def file_load_view(request):
    f = StringIO()
    writer = DictWriter(f,
                        ["SC_CODE", "SC_NAME", "SC_GROUP", "SC_TYPE", "OPEN",
                         "HIGH", "LOW", "CLOSE",
                         "LAST", "PREVCLOSE", "NO_TRADES", "NO_OF_SHRS",
                         "NET_TURNOV", "TDCLOINDI"]
                        )
    writer.writeheader()
    key = request.GET.get('SC_NAME')
    print(key)
    if key:
        values = conn.hgetall(key)
        writer.writerow({y.decode('ascii'): values.get(y).decode(
            'ascii') for y in values.keys()})
    else:

        for key in conn.keys('zerodha*'):
            values = conn.hgetall(key)
            data = {y.decode('ascii'): values.get(y).decode(
                'ascii') for y in values.keys()}
            writer.writerow(data)

    report = f.getvalue()

    resp = HttpResponse(report, content_type="application/octet-stream")
    resp["Content-Disposition"] = "attachment; filename='{}'".format(
        "report.csv")
    return resp

# Create your views here.
def index1(request):
    try:

        key = request.GET.get('SC_NAME')
        if key:
            values = conn.hgetall(key)
            data_list = [{y.decode('ascii'): values.get(y).decode(
                'ascii') for y in values.keys()}]
        else:
            data_list = []
            for key in conn.keys('zerodha*'):
                values = conn.hgetall(key)
                data = {y.decode('ascii'): values.get(y).decode(
                    'ascii') for y in values.keys()}
                data_list.append(data)

    except Exception as e:
        print(e)
        data_list = []

    return render(request, 'index.html', {"data_list": data_list})
