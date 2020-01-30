from zeep import Client
import jdatetime
def mobile_massage(reciver,content):
    sender="+985000131060"
    reciver="09352997106"
    # content="send massage module"
    print('this is an other massage')
    result=send_my_msg(sender,reciver,content)
    return result

def send_my_msg(sender,reciver,content):
    #ToDo: get sms webservice from data base
    user="rasa"
    password="78010"
    client=Client('http://185.4.31.182/class/sms/webservice2/server.php?wsdl')
    result_send_massage= client.service.SendSMS(sender, reciver, content, "",user,password)
    # get_creadit=client.service.GetCredit(user,password)
    # return get_creadit
    return result_send_massage



def jalali_str_to_gorgian_date(jalali_string):
        jdate_year=int(jalali_string[0:4])
        jdate_month=int(jalali_string[5:7])
        jdate_day=int(jalali_string[8:10])
        current_jdate=jdatetime.date(jdate_year, jdate_month, jdate_day)
        print('salam')
        return jdatetime.date.togregorian(current_jdate)

from datetime import datetime, timedelta

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start
    # return start if start > now else start + timedelta(days=1)  