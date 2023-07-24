from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import random 
import ipaddress
import string


fake=Faker()



logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# p=Producer({'bootstrap.servers':'localhost:9092'})
p=Producer({'bootstrap.servers':'195.201.19.174:9092'})
print('Kafka Producer has been initiated...')

def generate_job_id():
    #9159752-30920743-0-3-964
    job=random.randint(9000000, 9999999)
    sub=random.randint(30000000, 39999999)
    test=random.randint(0, 1)
    seeds=random.randint(0, 10)
    usr=random.randint(1, 999)
    return f"{job}-{sub}-{test}-{seeds}-{usr}"


def generate_fake_email():
    fake = Faker()
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
    domain = random.choice(domains)
    return fake.email(domain=domain)

def generate_fake_ip():
    # Define the IP address range you want to use for generating fake IPs
    start_ip = ipaddress.IPv4Address('192.168.0.1')
    end_ip = ipaddress.IPv4Address('192.168.0.255')

    # Generate a random IP address within the defined range
    fake_ip = ipaddress.IPv4Address(random.randint(int(start_ip), int(end_ip)))
    return str(fake_ip)

def generate_fake_domain():
    # You can customize the domain structure here
    prefixes = ['example', 'test', 'dummy', 'fake', 'sandbox']
    top_level_domains = ['.com', '.org', '.net', '.io']

    prefix = random.choice(prefixes)
    suffix = ''.join(random.choices(string.ascii_lowercase, k=5))  # Generating a random 5-letter suffix
    tld = random.choice(top_level_domains)

    return prefix + '.' + suffix + tld


def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def main():
    for i in range(10):
        # data={
        #    'email': generate_fake_email(),
        #    'vmta':generate_fake_domain() + '-' + generate_fake_ip(),
        #    'jobId': generate_job_id(),
        #    'timeLogged': str(fake.date_time_this_month())    
        #    }
        # m=json.dumps(data)
        m=f"{ str(fake.date_time_this_month()) },{ generate_fake_email() },{ generate_job_id() },{ generate_fake_domain() + '-' + generate_fake_ip() }"

        print(m)
        # print(m)
        p.poll(1)
        p.produce('pmta-delivered', m.encode('utf-8'),callback=receipt)
        p.flush()
        # time.sleep(1)

# 2023-07-23 09:41:00+0100,pgreenaway9@icloud.com,9159752-30920743-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,brfuga32@mac.com,9159752-30920744-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,decosta.jr@icloud.com,9159752-30920742-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,philiptav12@icloud.com,9159752-30920743-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,jareismommy@icloud.com,9159752-30920746-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,pitcher2008@icloud.com,9159752-30920743-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,debbijross@icloud.com,9159752-30920742-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,jacqueline.romero9@icloud.com,9159752-30920746-0-3-964,yab.mail.catcher.ru-45.79.69.46
# 2023-07-23 09:41:00+0100,tford1003@icloud.com,9159752-30920746-0-3-964,yab.mail.catcher.ru-45.79.69.46


if __name__ == "__main__":
    main()