from operator import itemgetter
import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# process information abou each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # build a dictionary for each articile
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
        reverse=True)

# When we get to here, the dictionary is sorted, so now
# use the dictionary to build information for our bar graph
submission_links, submission_comments, labels = [], [], []
for submission_dict in submission_dicts:
    submission_link =  f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    submission_links.append(submission_link)
    submission_comments.append(submission_dict['comments'])
    label = f"{submission_dict['title']}"
    labels.append(label)

# Make visualization
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': submission_comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)' }
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most Commented Articles',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Articles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='article_comments.html')
