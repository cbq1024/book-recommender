from recommenders.utils import general_utils
from recommenders.utils import gpu_utils
from recommenders.utils import spark_utils
from recommenders.utils import timer
from recommenders.utils import python_utils

"""
通用实用程序
"""


def get_number_processors():
    """Get the number of processors in a CPU.

    Returns:
        int: Number of processors.
    """
    return general_utils.get_number_processors()


def get_physical_memory():
    """Get the physical memory in GBs.

    Returns:
        float: Physical memory in GBs.
    """
    return general_utils.get_physical_memory()


def invert_dictionary(dictionary):
    """Invert a dictionary

    Note:

        If the dictionary has unique keys and unique values, the inversion would be perfect. However, if there are
        repeated values, the inversion can take different keys

    Args:
        dictionary (dict): A dictionary

    Returns:
        dict: inverted dictionary
    """
    return general_utils.invert_dictionary(dictionary)


def get_gpu_info():
    """Get information of GPUs.

    Returns:
        list: List of gpu information dictionary as with `device_name`, `total_memory` (in Mb) and `free_memory` (in Mb).
        Returns an empty list if there is no cuda device available.
    """
    return gpu_utils.get_gpu_info()


def get_number_gpus():
    """Get the number of GPUs in the system.
    Returns:
        int: Number of GPUs.
    """
    return gpu_utils.get_number_gpus()


def clear_memory_all_gpus():
    """Clear memory of all GPUs.
    """
    return gpu_utils.clear_memory_all_gpus()


def get_cuda_version():
    """Get CUDA version

    Returns:
        str: Version of the library.
    """
    return gpu_utils.get_cuda_version()


def get_cudnn_version():
    """Get the CuDNN version

    Returns:
        str: Version of the library.
    """
    return gpu_utils.get_cudnn_version()


def start_or_get_spark(
    app_name="Sample",
    url="local[*]",
    memory="10g",
    config=None,
    packages=None,
    jars=None,
    repositories=None,
):
    """Start Spark if not started

    Args:
        app_name (str): set name of the application
        url (str): URL for spark master
        memory (str): size of memory for spark driver. This will be ignored if spark.driver.memory is set in config.
        config (dict): dictionary of configuration options
        packages (list): list of packages to install
        jars (list): list of jar files to add
        repositories (list): list of maven repositories

    Returns:
        object: Spark context.
    """
    return spark_utils.start_or_get_spark(app_name, url, memory, config, packages, jars, repositories)


def get_timer_instance():
    return timer.Timer()


def start_timer(timer_instance):
    return timer_instance.start()


def stop_timer(timer_instance):
    return timer_instance.stop()


def binarize(a, threshold):
    """Binarize the values.

    Args:
        a (numpy.ndarray): Input array that needs to be binarized.
        threshold (float): Threshold below which all values are set to 0, else 1.

    Returns:
        numpy.ndarray: Binarized array.
    """
    return python_utils.binarize(a, threshold)


def cosine_similarity(cooccurrence):
    """Helper method to calculate the Cosine similarity of a matrix of
       co-occurrences.

       Cosine similarity can be interpreted as the angle between the i-th
       and j-th item.

       Args:
           cooccurrence (numpy.ndarray): The symmetric matrix of co-occurrences of items.

       Returns:
           numpy.ndarray: The matrix of cosine similarity between any two items.

       """
    return python_utils.cosine_similarity(cooccurrence)


def exponential_decay(value, max_val, half_life):
    """Compute decay factor for a given value based on an exponential decay.

       Values greater than `max_val` will be set to 1.

       Args:
           value (numeric): Value to calculate decay factor
           max_val (numeric): Value at which decay factor will be 1
           half_life (numeric): Value at which decay factor will be 0.5

       Returns:
           float: Decay factor
       """
    return python_utils.exponential_decay(value, max_val, half_life)


def get_top_k_scored_items(scores, top_k, sort_top_k=False):
    """Extract top K items from a matrix of scores for each user-item pair, optionally sort results per user.

      Args:
          scores (numpy.ndarray): Score matrix (users x items).
          top_k (int): Number of top items to recommend.
          sort_top_k (bool): Flag to sort top k results.

      Returns:
          numpy.ndarray, numpy.ndarray:
          - Indices into score matrix for each user's top items.
          - Scores corresponding to top items.

      """
    return python_utils.get_top_k_scored_items(scores, top_k, sort_top_k)


def inclusion_index(cooccurrence):
    """Helper method to calculate the Inclusion Index of a matrix of
       co-occurrences.

       Inclusion index measures the overlap between items.

       Args:
           cooccurrence (numpy.ndarray): The symmetric matrix of co-occurrences of items.

       Returns:
           numpy.ndarray: The matrix of inclusion index between any two items.

       """
    return python_utils.inclusion_index(cooccurrence)


def jaccard(cooccurrence):
    """Helper method to calculate the Jaccard similarity of a matrix of
        co-occurrences.  When comparing Jaccard with count co-occurrence
        and lift similarity, count favours predictability, meaning that
        the most popular items will be recommended most of the time. Lift,
        by contrast, favours discoverability/serendipity, meaning that an
        item that is less popular overall but highly favoured by a small
        subset of users is more likely to be recommended. Jaccard is a
        compromise between the two.

        Args:
            cooccurrence (numpy.ndarray): the symmetric matrix of co-occurrences of items.

        Returns:
            numpy.ndarray: The matrix of Jaccard similarities between any two items.

        """
    return python_utils.jaccard(cooccurrence)


def lexicographers_mutual_information(cooccurrence):
    """Helper method to calculate the Lexicographers Mutual Information of
       a matrix of co-occurrences.

       Due to the bias of mutual information for low frequency items,
       lexicographers mutual information corrects the formula by
       multiplying it by the co-occurrence frequency.

       Args:
           cooccurrence (numpy.ndarray): The symmetric matrix of co-occurrences of items.

       Returns:
           numpy.ndarray: The matrix of lexicographers mutual information between any two items.

       """
    return python_utils.lexicographers_mutual_information(cooccurrence)


def lift(cooccurrence):
    """Helper method to calculate the Lift of a matrix of
       co-occurrences. In comparison with basic co-occurrence and Jaccard
       similarity, lift favours discoverability and serendipity, as
       opposed to co-occurrence that favours the most popular items, and
       Jaccard that is a compromise between the two.

       Args:
           cooccurrence (numpy.ndarray): The symmetric matrix of co-occurrences of items.

       Returns:
           numpy.ndarray: The matrix of Lifts between any two items.

       """
    return python_utils.lift(cooccurrence)


def mutual_information(cooccurrence):
    """Helper method to calculate the Mutual Information of a matrix of
      co-occurrences.

      Mutual information is a measurement of the amount of information
      explained by the i-th j-th item column vector.

      Args:
          cooccurrence (numpy.ndarray): The symmetric matrix of co-occurrences of items.

      Returns:
          numpy.ndarray: The matrix of mutual information between any two items.

      """
    return python_utils.mutual_information(cooccurrence)


def rescale(data, new_min=0, new_max=1, data_min=None, data_max=None):
    """Rescale/normalize the data to be within the range `[new_min, new_max]`
      If data_min and data_max are explicitly provided, they will be used
      as the old min/max values instead of taken from the data.

      Note:
          This is same as the `scipy.MinMaxScaler` with the exception that we can override
          the min/max of the old scale.

      Args:
          data (numpy.ndarray): 1d scores vector or 2d score matrix (users x items).
          new_min (int|float): The minimum of the newly scaled data.
          new_max (int|float): The maximum of the newly scaled data.
          data_min (None|number): The minimum of the passed data [if omitted it will be inferred].
          data_max (None|number): The maximum of the passed data [if omitted it will be inferred].

      Returns:
          numpy.ndarray: The newly scaled/normalized data.
      """
    return python_utils.rescale(data, new_min, new_max, data_min, data_max)
