from datetime import datetime, timedelta
from core.dataPortal import DataPortal
from airflow.operators import PythonOperator



seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                  datetime.min.time())


def dataPortal(ds, **kwargs):
    # fdAd = FdaAdapter()
    # fdAd.processResponse(fdAd.getDsRequest())

    dp = DataPortal()
    dp.createDataPortal()


run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=dataPortal,
    dag=dag,
)
