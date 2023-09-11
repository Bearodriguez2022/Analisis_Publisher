from googleads import ad_manager
from datetime import datetime, timedelta
from googleads import errors
import tempfile




ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage(r'C:\Users\Usuario\openlifter\googleads.yaml')

#CONTROLAR YAML DIGA 'network_code : "Nº"' PARA QUE FUNCIONE
end_date = datetime.now().date()- timedelta(days=1)
start_date = end_date - timedelta(days=30)
report_job = {
    'reportQuery': {
        'dimensions': ['DATE', 'COUNTRY_NAME','AD_EXCHANGE_PRODUCT_NAME','DEVICE_CATEGORY_NAME',
                       'MOBILE_INVENTORY_TYPE','MOBILE_DEVICE_NAME',
                       ],
        'reportCurrency': 'USD',
        'columns': ['AD_EXCHANGE_TOTAL_REQUESTS','AD_EXCHANGE_TOTAL_IMPRESSIONS',
                    'AD_EXCHANGE_ACTIVE_VIEW_MEASURABLE_IMPRESSIONS',
                 
                  'AD_EXCHANGE_PRODUCT_NAME','AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE' ],
            
                 


        'dateRangeType': 'CUSTOM_DATE',
        'startDate': start_date,
        'endDate': end_date
    }
}


# Inicializa el DataDownloader.
report_downloader = ad_manager_client.GetDataDownloader(version='v202305')


try:

    report_job_id = report_downloader.WaitForReport(report_job)
except errors.AdManagerReportError as e:
    print('Error al generar el informe. Error: %s' % e)



report_file_path = 'report.csv'


export_format = 'CSV_DUMP'


report_file = tempfile.NamedTemporaryFile(suffix='aD.csv.gz', delete=False)

report_downloader.DownloadReportToFile(
    report_job_id, export_format, report_file)

report_file.close()
  # Display results.
print('Report job with id "%s" downloaded to:\n%s' % (
      report_job_id, report_file.name))