from Sortirovka import sort,get_da
from vievBD import get_number_operation,get_data
from read_file_stydent import  file_stydent
from main import sort_data


def button():
    return sort_data(get_number_operation,file_stydent,sort,get_da,get_data)
