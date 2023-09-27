from PythonExamples.home_asignment_notrafic.data_types import RLRRequest
from PythonExamples.home_asignment_notrafic.invokers import RequestInvokerBase

class RLR:
    def __init__(self, invoker: RequestInvokerBase):
        self.invoker = invoker

    def start_invoker(self):
        self.invoker.start()

    def calc_crossing_timestamp(self, request: RLRRequest):
        self.invoker.add_request(request)
