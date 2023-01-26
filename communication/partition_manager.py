class PartitionManager:
    def __init__(self,max_data_size=1024,old_data_interval_sec=3.0):
        """
        ctor
        :param max_data_size: max size of each partitioned data part
        :param old_data_interval_sec: when does a partitioned data part considered old and should be removed
        """
        self.old_data_interval_sec = old_data_interval_sec
        self.max_data_size = max_data_size
