import common_utils as utils


def general_utils_demo():
    print(f'the number of processors is {utils.get_number_processors()}')
    print(f'the memory of physical is {utils.get_physical_memory():.2f} GB')
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 1,
        'd': 3
    }
    print(f'source dictionary is {sample_dict}')
    print(f'invert dictionary is {utils.invert_dictionary(sample_dict)}')


def gpu_utils_demo():
    print(f'gpu info is {utils.get_gpu_info()}')
    print(f'gpu info is {utils.get_number_gpus()}')
    # utils.clear_memory_all_gpus()
    print(f'cuda version is {utils.get_cuda_version()}')
    print(f'cudnn version is {utils.get_cudnn_version()}')


def spark_utils_demo():
    spark_context = utils.start_or_get_spark()
    print(spark_context)


if __name__ == '__main__':
    # timer
    timer = utils.get_timer_instance()
    with timer as t:
        t.start()
        # general_utils_demo()
        # spark_utils_demo()
        # gpu_utils_demo()
        t.stop()
    print(f'the timer result is {float(t.__str__()):.2f} seconds')
