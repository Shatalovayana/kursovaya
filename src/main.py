from src.functions import load_operations, executed_operations,print_bank_info, date_operations, get_card_number_to, get_card_number_from
import json

loaded_data = load_operations('operations.json')
executed_data = executed_operations(loaded_data)
for operation in executed_data[:5]:
    print_bank_info(operation)

