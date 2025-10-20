"""
Naukri Job Scraper
Author: Your Name
Date: January 2025
Description: Scrapes job listings from Naukri.com based on role search

Requirements:
- playwright
- Python 3.x

Usage:
    python scraper.py
"""

from playwright.sync_api import sync_playwright,expect
import re
import csv
from datetime import datetime

def safe_locator(page,selector,timeout=10000):
    target=page.locator(selector).first
    try:
        if  target.is_visible(timeout=timeout):
            return target
    except Exception as e:
        print(f" locator of {target} ended with an exception {e}")
    return None

def safe_fill(target,fill_value):
    if not target:
        print(f'Fill Skipped locator not found or not visible')
        return
    try:
        target.fill(fill_value)
        print(f"Filled {target} with {fill_value}")
    except Exception as e:
        print(f"Failed to fill: {target},\nException:{e}")

def safe_text(locator):
        try:
            return locator.text_content() if locator.count()>0 else "No Data Found"
        except Exception as e :
            print(f'Exception Occured while extracting text: {e}')
            return 'No Data Found'


def search_job(role_name):
    if not role_name:
        print("No ROle Name Provided")
        return None
    
    with sync_playwright() as p:
        if role_name:
            browser=p.chromium.launch(headless=False,slow_mo=300)
            context=browser.new_context()
            try:
                naukri=context.new_page()
                naukri.goto('https://www.naukri.com/')
                naukri.wait_for_load_state('domcontentloaded')
                search_box=safe_locator(naukri,'.suggestor-box')
                if search_box:
                    search_input=search_box.get_by_placeholder(re.compile('Enter skills',re.IGNORECASE)).first
                    safe_fill(search_input,role_name)
                    search_button=safe_locator(naukri,'.qsbSubmit')

                    if search_button:
                        with naukri.expect_navigation(timeout=5000) :
                            search_button.click()
                        naukri.wait_for_load_state('networkidle')

                        print(naukri.title(),naukri.url)

                        job_list_container=naukri.locator(".srp-jobtuple-wrapper")
                        if job_list_container.count()==0:
                            print('JOB LIST CONTAINER IS EMPTY')
                            return
                        
                        jobs=job_list_container.filter(has=naukri.get_by_role("heading",name=re.compile(role_name,re.IGNORECASE)))

                        if jobs:
                            try:
                                timestamp=datetime.now().strftime('%Y%m%d_%H%M%S')
                                filename=f'{timestamp}_{role_name}.csv'
                                job_csv=open(filename,'w',newline='',encoding='utf-8')
                                csv_writer=csv.writer(job_csv)
                                csv_writer.writerow(['Job Title','Company Name','Experience','Location','Gender Preference','Job Description','Link'])
                                for job in jobs.all():
                                    job_title=safe_text(job.get_by_role("heading"))
                                    comp_span=job.locator('.row2 span').first
                                    exp=safe_text(job.locator('.expwdth'))
                                    loc=safe_text(job.locator('.locWdth'))
                                    gender_pref=safe_text(job.locator('.pill-container span'))
                                    comp_name=comp_span.get_by_role("link").first.inner_text()
                                    job_desc=safe_text(job.locator('.row4 span').first)
                                    link=comp_span.get_by_role("link").first.get_attribute('href')

                                    csv_writer.writerow([job_title,comp_name,exp,loc,gender_pref,job_desc,link])
                                    # print(f"Job Title: {job_title},Company Name:{comp_name},Description:{job_desc},link:{link}\n")
                            except Exception as e:
                                print(f'Exception occured when writing in csv file :{e}')
                            finally:
                                job_csv.close()
                            
                        
                        
                else:
                    print("No search_box found")
            except Exception as e:
                print(f'Exception in Search Job : {e}')
            finally:
                context.close()
                browser.close()
        else:
            print("No role name provided")  


search_job("Python Developer")