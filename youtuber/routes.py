from flask import render_template,redirect,url_for
from youtuber import db ,app
from youtuber.controller import Scraper
from datetime import datetime
from youtuber.models import Info
from datetime import datetime
import youtube_dl
import zipfile
import os




scraper = Scraper('https://www.youtube.com')

@app.route('/')
def home_page():
    infos = Info.query.all()
    compress_time_checker()
    if not infos:
        scraper.web_progress()
    first_info = Info.query.get_or_404(1)
    posted_date = first_info.date_posted
    date_now = datetime.now()
    difference = date_now - posted_date
    #To update check file insertion is more than 7 hours or not
    if int(difference.total_seconds() // 60**2) >= 1:
        db.drop_all()
        db.create_all()
        scraper.web_progress()
    
    return render_template('main.html', infos=infos)


@app.route('/download/<int:id>')
def download_video(id):
    info = Info.query.get_or_404(id)
    link = [info.url]
    ydl_opts = {
                'format' : 'best',
                'outtmpl' :'youtuber/static/videos/%(title)s.%(ext)s',
                
                }

    with youtube_dl.YoutubeDL(ydl_opts) as yld:
            yld.download(link)
    # To zip and compress your file
    with zipfile.ZipFile(f"youtuber/static/videos/{info.title}.zip", 'w',compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write(f"youtuber/static/videos/{info.title}.mp4")
    # To store file to designated directory
    file_path = app.config['UPLOAD_FILE']+ f"{info.title}.zip"
    with open(os.path.join(os.path.dirname(__file__),file_path),'rb') as file:
        content= file.read()
        info.file = content
        info.video_downloaded_at = datetime.now()
        db.session.commit()
    # comment two linew below if you want the vidoes appear on your working directory
    os.remove(app.config['UPLOAD_FILE']+f"{info.title}.mp4")
    os.remove(app.config['UPLOAD_FILE']+f"{info.title}.zip")
    
    return redirect(url_for('home_page'))

@app.route('/delete/<int:id>')
def delete_video(id):
    info = Info.query.get_or_404(id)
    info.file = None
    info.video_downloaded_at = None
    db.session.commit()
    return redirect(url_for('home_page'))
    
  
# To check dowloaded files expiration date
def compress_time_checker():
    infos = Info.query.all()
    date_now = datetime.now()
    for info in infos:
        if info.video_downloaded_at:
            diff = date_now - info.video_downloaded_at
            if int(diff.total_seconds() // 60**2) >= 1:
                  info.file = None
                  info.video_downloaded_at = None
                  db.session.commit()
    return redirect(url_for('home_page'))              
                  
                        
    
    

    



