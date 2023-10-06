from apscheduler.schedulers.blocking import BlockingScheduler
from source.web_scrappers.WebScrapper import WebScrapper
from db_op import cursor, conn
from mailgun import send_email_via_mailgun

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)  # 每24小时执行一次
def timed_job():
    def timed_job():
        # 1. 获取所有用户及其URL
        try:
            cursor.execute("SELECT email, url FROM users")
            users = cursor.fetchall()
        except Exception as e:
            print(f"Error fetching from database: {e}")
            return

        # 2. 对每个用户的URL进行爬取
        for user in users:
            email, user_url = user
            try:
                webScrapper = WebScrapper(user_url)
                results = webScrapper.call_scrapper()
            except Exception as e:
                print(f"Error during web scraping for {user_url}: {e}")
                continue

            description, url, price, site = [], [], [], []

            for result in results:
                if result:
                    try:
                        if price_min <= float(result['price'][1:]) <= price_max:
                            description.append(result['description'])
                            url.append(result['url'])
                            price.append(float(result['price'].strip('$').rstrip('0')))
                            site.append(result['site'])
                    except Exception as e:
                        print(f"Error processing scraped data: {e}")
                        continue

            # 3. 发送邮件给用户
            if len(price):
                subject = "Your cheapBuy Results Update"
                email_content = f"Here are the updated results for {user_url}:\n\n"
                for s, u, p in zip(site, url, price):
                    email_content += f"Website: {s}, Price: ${p}, Link: {u}\n"

                try:
                    send_email_via_mailgun(email, subject, email_content)
                except Exception as e:
                    print(f"Error sending email to {email}: {e}")


sched.start()
