import logging
import datetime


def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger('time_log_analyze')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('hb_test.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(file_handler)
    return logger

def parse_timestamp(line, target_key):
    if target_key in line:
        timestamp_start_index = line.find("Timestamp ")
        if timestamp_start_index != -1:
            time_str_start = timestamp_start_index + 10
            time_str_end = time_str_start + 8
            timestamp_str = line[time_str_start:time_str_end]
            try:
                return datetime.datetime.strptime(timestamp_str, "%H:%M:%S").time()
            except ValueError:
                print(f'Error while parsing timestamp: {line.strip()}')
    return None

def read_and_filter_log(filename, target_key, logger):

    filtered_log = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                timestamp_obj = parse_timestamp(line, target_key)
                if timestamp_obj:
                    filtered_log.append(timestamp_obj)
    except FileNotFoundError:
        logger.error('File not found:', filename)
        return None
    return filtered_log

def analyze_heartbeat_intervals(filtered_log, logger, target_key):

    if not filtered_log:
        logger.info(f'No entries with target key {target_key} found')
        return

    for i in range(len(filtered_log) - 1):
        current_timestamp = filtered_log[i]
        next_timestamp = filtered_log[i + 1]

        dt_current = datetime.datetime.combine(datetime.date.today(), current_timestamp)
        dt_next = datetime.datetime.combine(datetime.date.today(), next_timestamp)

        time_diff = abs(dt_current - dt_next).total_seconds()

        if 31 < time_diff < 33:
            logger.warning(f'Heartbeat {time_diff:.2f} sec. between {current_timestamp} and {next_timestamp}')
        elif time_diff >= 33:
            logger.error(f'Heartbeat {time_diff:.2f} sec. between {current_timestamp} and {next_timestamp}')

def time_log_analyzer_main(filename):

    logger = setup_logger('time_log_analyzer', 'hb_test.log')
    target_key = "TSTFEED0300|7E3E|0400"

    filtered_timestamps = read_and_filter_log(filename, target_key, logger)

    if filtered_timestamps is not None:
        if not filtered_timestamps:
            logger.info(f'No recorde with this key: {target_key} in file: {filename}')
            return
        analyze_heartbeat_intervals(filtered_timestamps, logger, target_key)


if __name__ == '__main__':
    time_log_analyzer_main('hblog.txt')
