from googleads import ad_manager
from datetime import datetime, timedelta
from googleads import errors
import tempfile




ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage(r'C:\Users\Usuario\openlifter\googleads.yaml')


# Set the start and end dates of the report to run (past 30 days).
end_date = datetime.now().date()- timedelta(days=1)
start_date = end_date - timedelta(days=30)
#currencyCode: ['SecondaryCurrencyCode']
report_job = {
    'reportQuery': {
        'dimensions': ['DATE','BID_RANGE','BID_REJECTION_REASON_NAME'],
        #'dimensionAttributes': ['LINE_ITEM_CURRENCY_CODE'],'SECONDARY_CURRENCY_CODE'
        'reportCurrency': 'USD',
        'columns': ['BID_COUNT','BID_AVERAGE_CPM',
                    ],
                       

        'dateRangeType':'CUSTOM_DATE',
        'startDate': start_date,
        'endDate': end_date
        
    
        },
    }

# Inicializa el DataDownloader.
report_downloader = ad_manager_client.GetDataDownloader(version='v202305')


try:
    # Ejecuta el informe y espera a que finalice.
    report_job_id = report_downloader.WaitForReport(report_job)
except errors.AdManagerReportError as e:
    print('Error al generar el informe. Error: %s' % e)

#down report
#report_file_path = 'report.csv'
# Change to your preferred export format.
export_format = 'CSV_DUMP'
report_file = tempfile.NamedTemporaryFile(suffix='bid4.csv.gz', delete=False)
# Download report data.
report_downloader.DownloadReportToFile(
    report_job_id, export_format, report_file)
report_file.close()
# Display results.
print('Report job with id "%s" downloaded to:\n%s' % (
      report_job_id, report_file.name))