import logging

car_logger = logging.getLogger('Car Logger')
car_logger.setLevel(logging.DEBUG)

log_formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')

car_handler = logging.FileHandler('Car.log')
car_handler.setLevel(logging.DEBUG)
car_handler.setFormatter(log_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)

car_logger.addHandler(car_handler)
car_logger.addHandler(stream_handler)
