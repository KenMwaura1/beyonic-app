import beyonic
import os
from dotenv import load_dotenv

load_dotenv()
beyonic.api_key = os.environ.get('BEYONIC_API_KEY')

payment = beyonic.Payment.create(phonenumber='+80000000001',
                                 payment_type='airtime',
                                 first_name='Kennedy',
                                 last_name='Amani',
                                 amount='1200',
                                 currency='BXC',
                                 description='Per diem',
                                 callback_url='https://my.website/payments/callback',
                                 metadata={'id': '134', 'name': 'Luc'}
                                 )

# print(payment)  # Examine the returned object

# print(beyonic.Payment.list())