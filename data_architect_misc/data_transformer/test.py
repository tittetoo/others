import pdb
import transform_errors
import transform_utils

if __name__ == '__main__':
    config = {
        'row_index_to_extract_column_names': 0,
        #'custom_column_names_to_assign': ['a','b'],
        'list_of_column_indexes_to_use':['int_id_1_1_1',
                                         'date_2019-01-01_2019-12-31_2',
                                         'ascii_str_8_8_3',
                                         'integer_-1000_1000_5'
                                         ],
        'old_column_name_to_new_column_name_mappings': {
            'int_id_1_1_1': 'col A',
            'date_2019-01-01_2019-12-31_2': 'col B',
            'ascii_str_8_8_3': 'col C',
            'integer_-1000_1000_5': 'col D'
        },
        'num_of_rows_to_skip_from_the_bottom': 5,
        'max_rows_to_process_each_iteration': 50,
        'input_csv_file_delimiter': '|',
    }

    print(transform_utils.get_raw_column_names('csv_n.csv', config))

    config = {
        'row_index_to_extract_column_names': 4,
        #'custom_column_names_to_assign': ['a','b'],
        'input_csv_file_delimiter': '|',
    }
    print(transform_utils.get_raw_column_names('csv_d.csv', config))

    config = {
        'row_index_to_extract_column_names': 4,
        'custom_column_names_to_assign': ['a','b'],
        'input_csv_file_delimiter': '|',
    }
    print(transform_utils.get_raw_column_names('csv_d.csv', config))

    config = {
        'row_index_to_extract_column_names': 0,
        'input_csv_file_delimiter': '|',
    }
    print(transform_utils.get_raw_column_names('excel_n.xlsx', config))

    config = {
        'row_index_to_extract_column_names': 4,
        'input_csv_file_delimiter': '|',
    }
    print(transform_utils.get_raw_column_names('excel_d.xlsx', config))

    config = {
        'row_index_to_extract_column_names': 4,
        'custom_column_names_to_assign': ['a','b'],
        'input_csv_file_delimiter': '|',
    }
    print(transform_utils.get_raw_column_names('excel_d.xlsx', config))

    # df2=pd.read_csv('csv_d.csv',delimiter='|', skiprows=4, nrows=0)
    # df3=pd.read_excel('excel_n.xlsx', sheet_name=0, header=0, nrows=0)
    # df3=pd.read_excel('excel_d.xlsx', sheet_name=0, header=4, nrows=0)

