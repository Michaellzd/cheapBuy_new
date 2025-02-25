from apscheduler.schedulers.blocking import BlockingScheduler
from source.web_scrappers.WebScrapper import WebScrapper
from db_op import *
from mailgun import send_email_via_mailgun

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=10)  #10s to parse
def timed_job():
    print("start time job")
    # 1. url user
    try:
        conn, cursor = create_connection()
        cursor.execute("SELECT email, url FROM users")
        users = cursor.fetchall()
        close_connection(cursor,conn)
        print(users)
    except Exception as e:
        print(f"Error fetching from database: {e}")
        return

    # 2. parse url
    for user in users:
        email, user_url = user
        print(email)
        print(user_url)

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
                    if 0.0 <= float(result['price'][1:]) <= float('inf'):
                        description.append(result['description'])
                        url.append(result['url'])
                        price.append(float(result['price'].strip('$').rstrip('0')))
                        site.append(result['site'])
                except Exception as e:
                    print(f"Error processing scraped data: {e}")
                    continue

        # 3. send email
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
