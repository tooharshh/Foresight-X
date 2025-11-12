from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('earthquake_data.csv', skiprows=1)
    df['Magnitude'] = df['Magnitude'].str.extract(r'([\d.]+)').astype(float)
    
    total_events = len(df)
    max_magnitude = df['Magnitude'].max()
    avg_magnitude = df['Magnitude'].mean()
    recent_event = df.iloc[0]['Location']
    
    return render_template('index.html', 
                         total_events=total_events,
                         max_magnitude=max_magnitude,
                         avg_magnitude=avg_magnitude,
                         recent_event=recent_event)

@app.route('/all-events')
def all_events():
    return render_template('all_events.html')

@app.route('/major-events')
def major_events():
    return render_template('major_events.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/stats')
def stats():
    df = pd.read_csv('earthquake_data.csv', skiprows=1)
    df['Magnitude'] = df['Magnitude'].str.extract(r'([\d.]+)').astype(float)
    df['Depth'] = pd.to_numeric(df['Depth'], errors='coerce')
    
    top_10 = df.nlargest(10, 'Magnitude')[['Origin Time', 'Location', 'Magnitude', 'Depth']]
    
    return render_template('stats.html', tables=[top_10.to_html(classes='data', index=False)])

if __name__ == '__main__':
    app.run(debug=True)
