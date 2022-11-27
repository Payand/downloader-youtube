from datetime import datetime
from youtuber import db



class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(300), nullable=False)
    duration = db.Column(db.String(300), nullable=True)
    url = db.Column(db.String(300), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    file = db.Column(db.String())
    video_downloaded_at = db.Column(db.DateTime, nullable=True)
    
    
    def __repr__(self):
        return f"Info('{self.title}','{self.date}','{self.date_posted}','{self.duration}','{self.url}','{self.file}')"