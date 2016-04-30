import logger

__author__ = "Brian Schkerke"
__copyright__ = "Copyright 2016 Brian Schkerke"
__license__ = "MIT"


class ProgressTracker(object):
    item_count_current = 0
    item_count_total = 0

    download_size_current = 0
    download_size_total = 0

    current_product = ""
    current_subproduct = ""
    current_download = ""

    @staticmethod
    def assign_download(hd):
        ProgressTracker.current_product = hd.product_name
        ProgressTracker.current_subproduct = hd.subproduct_name
        ProgressTracker.current_download = hd.machine_name

    @staticmethod
    def display_summary():
        progress_message = "%d/%d DL: %s/%s (%s)" % (ProgressTracker.item_count_current,
            ProgressTracker.item_count_total,
            ProgressTracker.format_filesize(ProgressTracker.download_size_current),
            ProgressTracker.format_filesize(ProgressTracker.download_size_total),
            ProgressTracker.format_percentage(ProgressTracker.download_size_current,
                                              ProgressTracker.download_size_total))

        logger.display_message(False, "Progress", progress_message)
        logger.display_message(True, "Progress", "%s: %s: %s" % (ProgressTracker.current_product, ProgressTracker.current_subproduct, ProgressTracker.current_download))

    @staticmethod
    def reset():
        ProgressTracker.item_count_total = 0
        ProgressTracker.item_count_current = 0
        ProgressTracker.download_size_current = 0
        ProgressTracker.download_size_total = 0
        ProgressTracker.current_product = ""
        ProgressTracker.current_subproduct = ""
        ProgressTracker.current_download = ""

    @staticmethod
    def format_filesize(filesize):
        prefixes = ['B', 'Kb', 'Mb', 'Gb', 'Tb']
        index_level = 0

        while abs(filesize / 1024) > 0:
            index_level += 1
            filesize /= 1024

        return "%d%s" % (filesize, prefixes[index_level])

    @staticmethod
    def format_percentage(current, total):
        if total == 0:
            return "0.00%"
        else:
            return '{percent:.2%}'.format(percent=(1.0 * current)/total)