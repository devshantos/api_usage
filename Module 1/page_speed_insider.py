import requests
url = 'https://csemcq.com/'
api_key = 'AIzaSyB6-NPOI1e4_bizKuZ-DGpzBpJqxJRTwDc'
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}'
data = requests.get(api_url)
data_track = data
if data.status_code == 200:
    your_website = data.json().get('loadingExperience').get('id')
    percentile = data.json().get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
    category = data.json().get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('category')
    step_link = 'https://blog.hubspot.com/website/how-to-optimize-website-speed'
    if category == 'FAST':
        article = f'You\'re website is very {category}. Your website is {your_website}. Website speed percentile is {percentile}. Good luck for you.'
        print(article)
    else:
        print(f'You\'re website is very {category}. Your website is {your_website}. Website speed percentile is {percentile}. Good luck for you. You should need to improve in your speed insight. Here\'s many steps to improve your site. Check it {step_link}')




