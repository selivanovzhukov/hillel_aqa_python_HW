import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    filename='group_search.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

def find_incoming_by_group_number(xml_file_path, target_number=None):
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and (target_number is None or number.text == str(target_number)):
                timing = group.find('timingExbytes')
                if timing is not None:
                    incoming = timing.find('incoming')
                    if incoming is not None:
                        result = incoming.text
                        logging.info(f"Incoming value for group {target_number}: {result}")
                        return result
                logging.info(f"No <incoming> tag found for group {target_number}")
                return None
        logging.info(f"No group found with number {target_number}")
        return None
    except ET.ParseError as e:
        logging.error(f"XML parse error: {e}")
        return None
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return None


find_incoming_by_group_number(r"\lesson_13\work_with_xml\groups.xml", target_number=4)
