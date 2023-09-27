from typing import Optional

from PythonExamples.home_asignment_notrafic import data_types
from PythonExamples.home_asignment_notrafic.data_types import Coord, TimedCoord
from PythonExamples.home_asignment_notrafic.invokers import RLRRequestInvoker
from PythonExamples.home_asignment_notrafic.persistence import PersistenceToFile
from PythonExamples.home_asignment_notrafic.request_processor import RLRRequestProcessor
from PythonExamples.home_asignment_notrafic.rlr import RLR

class Main:
    """application entry point, construct classes dependencies and run application"""

    def __init__(self):
        self.rlr: Optional[RLR] = None

    def construct(self):
        filename = 'crossing_events.txt'
        processor = RLRRequestProcessor()
        persistence = PersistenceToFile(filename, is_clean_file=True)
        invoker = RLRRequestInvoker(processor=processor, persistence=persistence)
        self.rlr = RLR(invoker=invoker)

    def run(self):
        self.rlr.start_invoker()

if __name__ == '__main__':
    main = Main()
    main.construct()
    main.run()

    # simulate 10 requests
    for i in range(10):
        req = data_types.RLRRequest(car_id=i,
                                    stop_line_coordinates=[Coord(5, 20), Coord(15, 20)],
                                    trajectory=[TimedCoord(6, 5, 10), TimedCoord(7, 15 + i, 15), TimedCoord(8, 30, 22)])
        main.rlr.calc_crossing_timestamp(req)
    input('press Enter to exit')
