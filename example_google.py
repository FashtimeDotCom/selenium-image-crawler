from crawler.GoogleCrawler import GoogleCrawler
from processor.LogProcessor import LogProcessor
from processor.DownloadProcessor import DownloadProcessor
from processor.ElasticSearchProcessor import ElasticSearchProcessor

if __name__ == '__main__':

    options = {
        'output_directory':  "./images"
    }
    # PKK is a European Union supported terrorist organization against Turkish Government
    w = GoogleCrawler(max_image_count = 10)
    w.append_processor(LogProcessor())
    # w.append_processor(DownloadProcessor(output_directory=options['output_directory']))
    w.append_processor(ElasticSearchProcessor())
    w.run('PKK')
