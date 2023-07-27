import requests
from py_zipkin.zipkin import zipkin_span
from py_zipkin.transport import BaseTransportHandler

from py_zipkin.transport import BaseTransportHandler


class HttpTransport(BaseTransportHandler):

    def get_max_payload_bytes(self):
        return None

    def send(self, encoded_span):
        # The collector expects a thrift-encoded list of spans.
        response = requests.post(
            'http://localhost:9411/api/v2/spans',
            data=encoded_span,
            headers={'Content-Type': 'application/x-thrift'},
        )
        print('Response status code:', response.status_code)
        print('Response text:', response.text)


# Create the transport handler instance
some_handler = HttpTransport()

# Define your function that performs some actions
def do_stuff(a, b):
    print(a + b)

# The function that uses zipkin_span for tracing
def some_function(a, b):
    with zipkin_span(
        service_name='my_service',
        span_name='my_span_name',
        transport_handler=some_handler,
        port=42,
        sample_rate=80.0,  # 80% of the requests will be traced
    ):
        do_stuff(a, b)

# Call the function
some_function(3, 5)
