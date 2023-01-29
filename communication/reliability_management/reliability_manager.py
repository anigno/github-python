# utc time to wait for ack
self.receive_timeout: int = TimeUtils.utc_timestamp() + receive_timeout_interval

self.partition_timeout = GenericEvent('partition_timeout')
